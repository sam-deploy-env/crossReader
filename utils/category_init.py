from models.Category import Category

def init_categories(category_repo, setting_repo):
    category_repo.delete_all()
    categories = []
    # Scratch
    number_scratch_m = setting_repo.get_number_scratch_m()
    number_scratch_f = setting_repo.get_number_scratch_f()
    order = 1
    for i in range(1, number_scratch_m+1):
        categories.append(Category("Scratch M", True, "S" + str(i), "M", order, True))
        order += 1
    for i in range(1, number_scratch_f+1):
        categories.append(Category("Scratch F", True, "S" + str(i), "F", order, True))
        order += 1

    # Categories
    categories.append(Category("Jeune M", False, "J", "M", order))
    order += 1
    categories.append(Category("Senior M", False, "S", "M", order))
    order += 1
    categories.append(Category("35+ M", False, "35+", "M", order))
    order += 1
    categories.append(Category("45+ M", False, "45+", "M", order))
    order += 1
    categories.append(Category("55+ M", False, "55+", "M", order))
    order += 1
    categories.append(Category("65+ M", False, "65+", "M", order))
    order += 1
    categories.append(Category("75+ M", False, "75+", "M", order))
    order += 1
    categories.append(Category("Jeune F", False, "J", "F", order))
    order += 1
    categories.append(Category("Senior F", False, "S", "F", order))
    order += 1
    categories.append(Category("35+ F", False, "35+", "F", order))
    order += 1
    categories.append(Category("45+ F", False, "45+", "F", order))
    order += 1
    categories.append(Category("55+ F", False, "55+", "F", order))
    order += 1
    categories.append(Category("65+ F", False, "65+", "F", order))
    order += 1
    categories.append(Category("75+ F", False, "75+", "F", order))
    order += 1

    # Oriol
    categories.append(Category("Oriol M", False, "O", "M", order, True))
    order += 1
    categories.append(Category("Oriol F", False, "O", "F", order, True))
    order += 1

    category_repo.insert_categories(categories)