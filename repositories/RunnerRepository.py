from models.Runner import Runner

class RunnerRepository:

    def __init__(self, session):
        self.session = session

    # GETTERS
    def get_all(self):
        return (
            self.session.query(Runner)
            .order_by(Runner.ranking)
            .all()
        )

    def get_runner_map(self):
        return {
            f"{runner.last_name}_{runner.first_name}": runner
            for runner in self.session.query(Runner).all()
        }

    def get_rewards_map(self, ids):
        return {
            runner.id: runner
            for runner in self.session.query(Runner)
                .filter(Runner.id.in_(ids))
                .all()
        }

    def get_all_rewards_in_scratch(self, race_label, sex, number):
        return (
            self.session.query(Runner)
            .filter(
                Runner.finish == True,
                Runner.race_label == race_label,
                Runner.sex == sex,
                Runner.sex_ranking <= number
            )
            .order_by(Runner.sex_ranking)
            .all()
        )

    def get_reward_in_category(self, race_label, category, sex, skip):
        runner = (
            self.session.query(Runner)
            .filter(
                Runner.finish == True,
                Runner.race_label == race_label,
                Runner.sex == sex,
                Runner.category == category,
                Runner.sex_ranking > skip
            )
            .order_by(Runner.category_ranking)
            .first()
        )
        return runner.id if runner else None

    def get_first_oriol(self, race_label, ids, sex):
        runner = (
            self.session.query(Runner)
            .filter(
                Runner.finish == True,
                Runner.race_label == race_label,
                Runner.sex == sex,
                Runner.oriol == True,
                ~Runner.id.in_(ids)
            )
            .order_by(Runner.ranking)
            .first()
        )
        return runner.id if runner else None

    # INSERT
    def insert_runners(self, runners):
        self.session.add_all(runners)
        self.session.commit()

    # UPDATE
    def update(self, runner):
        self.session.merge(runner)
        self.session.commit()

    # DELETE
    def delete_all(self):
        self.session.query(Runner).delete()
        self.session.commit()
