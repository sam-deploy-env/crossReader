import json
import aiofiles
import asyncio

from models.Runner import Runner

async def read_file(category_repo, runner_repo, filename):
    runners_in_file = await extract_data(filename)
    await asyncio.to_thread(process_categories, category_repo, runners_in_file)
    await asyncio.to_thread(process_runners, runner_repo, runners_in_file)


async def extract_data(filename):
    async with aiofiles.open(filename, "r", encoding="utf-8") as file:
        content = await file.read()
    return json.loads(content).get("runners", [])

def process_categories(category_repo, runners):
    seen = set()
    categories = []

    for runner in runners:
        cat = runner["category"]
        key = (cat["abbreviation"], cat["sex"])
        if key not in seen:
            seen.add(key)
            categories.append({"category" : cat["abbreviation"], "sex" : cat["sex"]})

    category_repo.bulk_enable(categories)


def process_runners(runner_repo, runners_in_file):
    runner_map = runner_repo.get_runner_map()
    runners_to_insert = []
    for runner in runners_in_file:
        runner_to_save = extract_runner(runner)
        name = runner_to_save.last_name + "_" + runner_to_save.first_name
        if name in runner_map:
            runner_in_db = runner_map[name]
            if runner_to_save.is_different(runner_in_db):
                runner_to_save.id = runner_in_db.id
                runner_repo.update(runner_to_save)
        else:
            runners_to_insert.append(runner_to_save)
    runner_repo.insert_runners(runners_to_insert)

def extract_runner(runner):
    last_name = runner.get("lastName")
    first_name = runner.get("firstName")
    sex = runner.get("sex")
    ranking = or_default(runner.get("ranking"), 0)
    category = extract_category_label(runner)
    category_ranking = or_default(runner.get("categoryRanking"), 0)
    sex_ranking = or_default(runner.get("sexRanking"), 0)
    bib_number = runner.get("bib")
    runner_time = or_default(runner.get("time"), "")
    oriol = runner.get("oriol")
    dnf = runner.get("dnf")
    finish = runner_time != "" and ranking != 0
    return Runner(last_name, first_name, sex, ranking, category, category_ranking,
                            sex_ranking, bib_number, runner_time, oriol, finish, dnf)

def extract_category_label(runner):
    category = runner.get("category")
    if category and category.get("abbreviation"):
        return category.get("abbreviation")
    return ""

def or_default(value, default):
    return value if value is not None else default

