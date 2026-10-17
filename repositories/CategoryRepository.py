from sqlalchemy import tuple_

from models.Category import Category

class CategoryRepository:

    def __init__(self, session):
        self.session = session

    # GETTERS
    def get_rewards(self):
        return (
            self.session.query(Category)
            .filter(
                Category.active == True
            )
            .order_by(Category.order)
            .all()
        )

    def get_no_scratch_no_oriol(self):
        return (
            self.session.query(Category)
            .filter(
                Category.scratch == False,
                Category.category != "O",
                Category.active == True
            )
            .order_by(Category.order)
            .all()
        )

    # INSERT
    def insert_categories(self, categories):
        self.session.add_all(categories)
        self.session.commit()

    # UPDATE
    def bulk_update(self, rewards):
        mapping = {(r.race_label, r.category, r.sex): r.runner_id for r in rewards}

        for (race_label, category, sex), runner_id in mapping.items():
            self.session.query(Category) \
            .filter_by(race_label=race_label, category=category, sex=sex) \
            .update({"runner": runner_id}, synchronize_session=False)
        self.session.commit()

    def bulk_enable(self, filters):
        tuples = [(f["race_label"], f["category"], f["sex"]) for f in filters]
        self.session.query(Category) \
            .filter(tuple_(Category.race_label, Category.category, Category.sex).in_(tuples)) \
            .update({"active": True}, synchronize_session=False)
        self.session.commit()

    # DELETE
    def delete_all(self):
        self.session.query(Category).delete()
        self.session.commit()
