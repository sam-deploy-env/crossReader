import json
import aiofiles

from repositories.RunnerRepository import RunnerRepository
from repositories.SettingRepository import SettingRepository
from models.Runner import Runner

runner_repository = RunnerRepository()
setting_repository = SettingRepository()

async def read_file(filename):
    runner_map = runner_repository.get_runner_map()
    runners_to_insert = []

    async with aiofiles.open(filename, "r", encoding="utf-8") as file:
        content = await file.read()
    data = json.loads(content)

    runners_in_file = data.get("runners", [])
    for runner in runners_in_file:
        runner_to_save = extract_runner(runner)
        name = runner_to_save.last_name + "_" + runner_to_save.first_name
        if name in runner_map:
            runner_in_db = runner_map[name]
            if runner_to_save.is_different(runner_in_db):
                runner_to_save.id = runner_in_db.id
                runner_repository.update(runner_to_save)
        else:
            runners_to_insert.append(runner_to_save)
    runner_repository.insert_runners(runners_to_insert)

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

