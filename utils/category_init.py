from repositories.CategoryRepository import CategoryRepository
from repositories.SettingRepository import SettingRepository
from models.Category import Category

category_repository = CategoryRepository()
setting_repository = SettingRepository()

def init_categories():
    category_repository.delete_all()
    categories = []
    # Scratch
    number_scratch_m = setting_repository.get_number_scratch_m()
    number_scratch_f = setting_repository.get_number_scratch_f()
    order = 1
    for i in range(1, number_scratch_m+1):
        categories.append(Category("Scratch M", True, "S" + str(i), "M", order))
        order += 1
    for i in range(1, number_scratch_f+1):
        categories.append(Category("Scratch F", True, "S" + str(i), "F", order))
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

    # Oriol
    categories.append(Category("Oriol M", False, "O", "M", order))
    order += 1
    categories.append(Category("Oriol F", False, "O", "F", order))
    order += 1

    category_repository.insert_categories(categories)