from datetime import datetime

from database import db

class Runner(db.Model):
    __tablename__ = "runners"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    last_name = db.Column(db.String(63), nullable=False)
    first_name = db.Column(db.String(63), nullable=False)
    sex = db.Column(db.String(7), nullable=False)
    ranking = db.Column(db.Integer)
    category = db.Column(db.String(63), nullable=False)
    category_ranking = db.Column(db.Integer)
    sex_ranking = db.Column(db.Integer)
    bib_number = db.Column(db.Integer)
    time = db.Column(db.String(63))
    oriol = db.Column(db.Boolean)
    finish = db.Column(db.Boolean)
    out = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, last_name, first_name, sex, ranking, category, category_ranking, sex_ranking, bib_number, time, oriol, finish, out):
        self.last_name = last_name
        self.first_name = first_name
        self.sex = sex
        self.ranking = ranking
        self.category = category
        self.category_ranking = category_ranking
        self.sex_ranking = sex_ranking
        self.bib_number = bib_number
        self.time = time
        self.oriol = oriol
        self.finish = finish
        self.out = out

    def get_time(self):
        new_time = self.time.split('.')[0]
        if new_time.startswith("00:"):
            new_time = new_time[3:]
        return new_time

    def to_json(self):
        return {
            "id": self.id,
            "name": self.last_name + " " + self.first_name,
            "sex": self.sex,
            "ranking": self.ranking,
            "category": self.category,
            "category_ranking": self.category_ranking,
            "sex_ranking": self.sex_ranking,
            "bib_number": self.bib_number,
            "time": self.get_time(),
            "oriol": self.oriol,
            "finish": self.finish,
            "out": self.out
        }

    def is_different(self, runner):
        return self.last_name != runner.last_name \
            or self.first_name != runner.first_name \
            or self.sex != runner.sex \
            or self.ranking != runner.ranking \
            or self.category != runner.category \
            or self.category_ranking != runner.category_ranking\
            or self.sex_ranking != runner.sex_ranking \
            or self.bib_number != runner.bib_number \
            or self.time != runner.time \
            or self.oriol != runner.oriol \
            or self.finish != runner.finish \
            or self.out != runner.out