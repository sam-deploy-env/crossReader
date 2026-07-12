from database import db

class Setting(db.Model):
    __tablename__ = "settings"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.String(63))
    state = db.Column(db.BigInteger)

    def __init__(self, data: str, state: int):
        self.data = data
        self.state = state