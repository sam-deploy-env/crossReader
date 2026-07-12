from models.Setting import Setting
from database import db

class SettingRepository:

    def __init__(self):
        pass

    # GETTERS
    @staticmethod
    def get_number_scratch_m():
        setting = Setting.query.filter(Setting.data=="number_scratch_m").first()
        return setting.state if setting else None

    @staticmethod
    def get_number_scratch_f():
        setting = Setting.query.filter(Setting.data=="number_scratch_f").first()
        return setting.state if setting else None
    
    @staticmethod
    def get_mail_sent():
        setting = Setting.query.filter(Setting.data=="mail_sent").first()
        return setting.state if setting else None

    @staticmethod
    def get_started():
        setting = Setting.query.filter(Setting.data=="started").first()
        return setting.state if setting else None

    # SETTERS
    @staticmethod
    def set_number_scratch_m(number):
        setting = Setting.query.filter(Setting.data=="number_scratch_m").first()
        if setting:
            setting.state = number
        else:
            setting = Setting("number_scratch_m", number)
        db.session.add(setting)
        db.session.commit()

    @staticmethod
    def set_number_scratch_f(number):
        setting = Setting.query.filter(Setting.data=="number_scratch_f").first()
        if setting:
            setting.state = number
        else:
            setting = Setting("number_scratch_f", number)
        db.session.add(setting)
        db.session.commit()

    @staticmethod
    def set_mail_sent(number):
        setting = Setting.query.filter(Setting.data=="mail_sent").first()
        if setting:
            setting.state = number
        else:
            setting = Setting("mail_sent", number)
        db.session.add(setting)
        db.session.commit()

    @staticmethod
    def set_started(state):
        setting = Setting.query.filter(Setting.data=="started").first()
        if setting:
            setting.state = state
        else:
            setting = Setting("started", state)
        db.session.add(setting)
        db.session.commit()