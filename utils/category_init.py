from models.Category import Category

def init_categories(category_repo, setting_repo):
    category_repo.delete_all()
    categories = []

    add_categories_from_race(setting_repo, categories, "5kms")
    add_categories_from_race(setting_repo, categories, "10kms")

    category_repo.insert_categories(categories)

def add_categories_from_race(setting_repo, categories, race):
    # Scratch
    number_scratch_m = setting_repo.get_number_scratch_m()
    number_scratch_f = setting_repo.get_number_scratch_f()
    order = 1
    for i in range(1, number_scratch_m + 1):
        categories.append(Category(race, "Scratch M", True, "S" + str(i), "M", order, True))
        order += 1
    for i in range(1, number_scratch_f + 1):
        categories.append(Category(race, "Scratch F", True, "S" + str(i), "F", order, True))
        order += 1

    if race == "5kms" : return

    # Categories
    categories.append(Category(race, "Jeune M", False, "J", "M", order))
    order += 1
    categories.append(Category(race, "Senior M", False, "S", "M", order))
    order += 1
    categories.append(Category(race, "35+ M", False, "35+", "M", order))
    order += 1
    categories.append(Category(race, "45+ M", False, "45+", "M", order))
    order += 1
    categories.append(Category(race, "55+ M", False, "55+", "M", order))
    order += 1
    categories.append(Category(race, "65+ M", False, "65+", "M", order))
    order += 1
    categories.append(Category(race, "75+ M", False, "75+", "M", order))
    order += 1
    categories.append(Category(race, "Jeune F", False, "J", "F", order))
    order += 1
    categories.append(Category(race, "Senior F", False, "S", "F", order))
    order += 1
    categories.append(Category(race, "35+ F", False, "35+", "F", order))
    order += 1
    categories.append(Category(race, "45+ F", False, "45+", "F", order))
    order += 1
    categories.append(Category(race, "55+ F", False, "55+", "F", order))
    order += 1
    categories.append(Category(race, "65+ F", False, "65+", "F", order))
    order += 1
    categories.append(Category(race, "75+ F", False, "75+", "F", order))
    order += 1

    # Oriol
    categories.append(Category(race, "Oriol M", False, "O", "M", order, True))
    order += 1
    categories.append(Category(race, "Oriol F", False, "O", "F", order, True))
    order += 1