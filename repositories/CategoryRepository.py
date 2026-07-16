from models.Category import Category

class CategoryRepository:

    def __init__(self, session):
        self.session = session

    # GETTERS
    def get_rewards(self):
        return (
            self.session.query(Category)
            .order_by(Category.order)
            .all()
        )

    def get_by_sex(self, sex):
        return (
            self.session.query(Category)
            .filter(
                Category.sex == sex,
                Category.scratch == False,
                Category.category != "O"
            )
            .order_by(Category.order)
            .all()
        )

    def get_no_scratch_no_oriol(self):
        return (
            self.session.query(Category)
            .filter(
                Category.scratch == False,
                Category.category != "O"
            )
            .order_by(Category.order)
            .all()
        )

    # INSERT
    def insert_categories(self, categories):
        self.session.add_all(categories)
        self.session.commit()

    # UPDATE
    def update(self, reward):
        (
            self.session.query(Category)
            .filter_by(category=reward.category, sex=reward.sex)
            .update({"runner": reward.id})
        )
        self.session.commit()

    # DELETE
    def delete_all(self):
        self.session.query(Category).delete()
        self.session.commit()
