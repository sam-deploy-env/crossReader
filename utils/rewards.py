from utils import word_generator

def update_rewards(category_repo, runner_repo, setting_repo):
    rewards = get_rewards_in_db(category_repo, runner_repo, setting_repo)
    category_repo.bulk_update(rewards)
    if None not in [reward.runner_id for reward in rewards] and setting_repo.get_file_sent() == 0:
        word_generator.create_word_file(category_repo, runner_repo)
        return True
    return False

def get_rewards_in_db(category_repo, runner_repo, setting_repo):
    number_scratch_m = setting_repo.get_number_scratch_m()
    number_scratch_f = setting_repo.get_number_scratch_f()
    rewards = []
    for race_label in ["5kms", "10kms"]:
        get_rewards_in_scratch(rewards, race_label, 'M', number_scratch_m, runner_repo)
        get_rewards_in_scratch(rewards, race_label, 'F', number_scratch_f, runner_repo)
        categories = category_repo.get_no_scratch_no_oriol()
        for category in categories:
            number_scratch = number_scratch_f if category.sex == 'F' else number_scratch_m
            get_rewards_in_category(rewards, race_label, category.category, category.sex, number_scratch, runner_repo)
        ids_rewarded = [reward.runner_id for reward in rewards if reward.runner_id is not None]
        oriol_id_f = runner_repo.get_first_oriol(race_label, ids_rewarded, 'F')
        add_runner_in_rewards(rewards, oriol_id_f, race_label, "O", 'F')
        oriol_id_m = runner_repo.get_first_oriol(race_label, ids_rewarded, 'M')
        add_runner_in_rewards(rewards, oriol_id_m, race_label, "O", 'M')
    return rewards

def get_rewards_in_scratch(rewards, race_label, sex, number, runner_repo):
    scratch_runners = runner_repo.get_all_rewards_in_scratch(race_label, sex, number)
    for runner in scratch_runners:
        category = "S" + str(runner.sex_ranking)
        add_runner_in_rewards(rewards, runner.id, race_label, category, sex)

def get_rewards_in_category(rewards, race_label, category, sex, skip, runner_repo):
    runner_id = runner_repo.get_reward_in_category(race_label, category, sex, skip)
    add_runner_in_rewards(rewards, runner_id, race_label, category, sex)

def add_runner_in_rewards(rewards, runner_id, race_label, category, sex):
    if runner_id:
        reward = RewardInBase(race_label, category, sex, runner_id)
    else:
        reward = RewardInBase(race_label, category, sex, None)
    rewards.append(reward)

def get_rewards_to_display(category_repo, runner_repo):
    rewards = []
    rewards_in_db = category_repo.get_rewards()
    ids = [reward.runner for reward in rewards_in_db]
    runners = runner_repo.get_rewards_map(ids)
    for reward in rewards_in_db:
        runner = runners.get(reward.runner)
        if runner:
            rewards.append(RewardToDisplay(reward.race_label, reward.category, reward.sex, runner.ranking, runner.last_name, runner.first_name, runner.bib_number, runner.get_time()))
        else:
            rewards.append(RewardToDisplay(reward.race_label, reward.category, reward.sex))
    return rewards

class RewardInBase:
    
    def __init__(self, race_label, category: str, sex: str, runner_id: int = None):
        self.race_label = race_label
        self.category: str = category
        self.sex: str = sex
        self.runner_id: int = runner_id

class RewardToDisplay:
    
    def __init__(self, race_label: str, category: str, sex: str, ranking: int = None, last_name: str = None, first_name: str = None, bib_number: int = None, time: str = None):
        self.race_label = race_label
        self.category: str = category
        self.sex: str = sex
        self.ranking: int = ranking
        self.last_name: str = last_name
        self.first_name: str = first_name
        self.bib_number: int = bib_number
        self.time: str = time