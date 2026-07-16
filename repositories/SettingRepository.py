from models.Setting import Setting

class SettingRepository:

    def __init__(self, session):
        self.session = session

    # GETTERS
    def get_number_scratch_m(self):
        setting = (
            self.session.query(Setting)
            .filter(Setting.data == "number_scratch_m")
            .first()
        )
        return setting.state if setting else None

    def get_number_scratch_f(self):
        setting = (
            self.session.query(Setting)
            .filter(Setting.data == "number_scratch_f")
            .first()
        )
        return setting.state if setting else None

    def get_mail_sent(self):
        setting = (
            self.session.query(Setting)
            .filter(Setting.data == "mail_sent")
            .first()
        )
        return setting.state if setting else None

    def get_started(self):
        setting = (
            self.session.query(Setting)
            .filter(Setting.data == "started")
            .first()
        )
        return setting.state if setting else None

    # SETTERS
    def set_number_scratch_m(self, number):
        setting = (
            self.session.query(Setting)
            .filter(Setting.data == "number_scratch_m")
            .first()
        )
        if setting:
            setting.state = number
        else:
            setting = Setting("number_scratch_m", number)

        self.session.add(setting)
        self.session.commit()

    def set_number_scratch_f(self, number):
        setting = (
            self.session.query(Setting)
            .filter(Setting.data == "number_scratch_f")
            .first()
        )
        if setting:
            setting.state = number
        else:
            setting = Setting("number_scratch_f", number)

        self.session.add(setting)
        self.session.commit()

    def set_mail_sent(self, number):
        setting = (
            self.session.query(Setting)
            .filter(Setting.data == "mail_sent")
            .first()
        )
        if setting:
            setting.state = number
        else:
            setting = Setting("mail_sent", number)

        self.session.add(setting)
        self.session.commit()

    def set_started(self, state):
        setting = (
            self.session.query(Setting)
            .filter(Setting.data == "started")
            .first()
        )
        if setting:
            setting.state = state
        else:
            setting = Setting("started", state)

        self.session.add(setting)
        self.session.commit()
