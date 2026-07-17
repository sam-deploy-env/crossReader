from database import db

class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(63), nullable=False)
    scratch = db.Column(db.Boolean, nullable=False)
    category = db.Column(db.String(63), nullable=False)
    sex = db.Column(db.String(7), nullable=False)
    order = db.Column(db.Integer)
    active = db.Column(db.Boolean, nullable=False)
    runner = db.Column(db.Integer)

    def __init__(self, label, scratch, category, sex, order, active=False, runner=None):
        self.label = label
        self.scratch = scratch
        self.category = category
        self.sex = sex
        self.order = order
        self.runner = runner
        self.active = active

    def to_json(self):
        return {
            "label": self.label,
            "scratch": self.scratch,
            "category": self.category,
            "sex": self.sex,
            "order": self.order,
            "runner": self.runner
        }