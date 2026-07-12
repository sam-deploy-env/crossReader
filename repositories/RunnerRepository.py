from models.Runner import Runner
from database import db

class RunnerRepository:

    def __init__(self):
        pass

    # GETTERS
    @staticmethod
    def get_all():
        return Runner.query.order_by(Runner.ranking).all()

    @staticmethod
    def get_runner_map():
        return {runner.last_name + "_" + runner.first_name: runner for runner in Runner.query.all()}

    @staticmethod
    def get_rewards_map(ids):
        return {runner.id: runner for runner in Runner.query.filter(Runner.id.in_(ids)).all()}

    @staticmethod
    def get_reward_in_scratch(ranking, sex):
        runner = Runner.query.filter(Runner.finish == True, Runner.sex_ranking == ranking, Runner.sex == sex).first()
        if runner:
            return runner.id
        return None
    
    @staticmethod
    def get_reward_in_category(category, sex, skip):
        runner = Runner.query.filter(Runner.finish == True, Runner.sex == sex, Runner.category == category, Runner.sex_ranking > skip).order_by(Runner.category_ranking).first()
        if runner:
            return runner.id
        return None

    @staticmethod
    def get_first_oriol(ids, sex):
        runner = Runner.query.filter(Runner.finish == True, Runner.sex == sex, Runner.oriol == True, ~Runner.id.in_(ids)).order_by(Runner.ranking).first()
        if runner:
            return runner.id
        return None
    
    #INSERT
    @staticmethod
    def insert_runners(runners):
        db.session.add_all(runners)
        db.session.commit()

    # SETTERS
    @staticmethod
    def update(runner):
        db.session.merge(runner)
        db.session.commit()

    # DELETE
    @staticmethod
    def delete_all():
        Runner.query.delete()
        db.session.commit()
