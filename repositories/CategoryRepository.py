from unicodedata import category
from models.Category import Category
from database import db

class CategoryRepository:

    def __init__(self):
        pass

    # GETTERS
    @staticmethod
    def get_rewards():
        return Category.query.order_by(Category.order).all()

    @staticmethod
    def get_by_sex(sex):
        return Category.query.filter(Category.sex==sex, Category.scratch==False, Category.category!="O").order_by(Category.order).all()

    @staticmethod
    def get_no_scratch_no_oriol():
        return Category.query.filter(Category.scratch==False, Category.category!="O").order_by(Category.order).all()

    # INSERT
    @staticmethod
    def insert_categories(categories):
        db.session.add_all(categories)
        db.session.commit()

    # UPDATE
    @staticmethod
    def update(reward):
        Category.query.filter_by(category=reward.category, sex=reward.sex).update({"runner": reward.id})
        db.session.commit()

    # DELETE
    @staticmethod
    def delete_all():
        Category.query.delete()
        db.session.commit()
