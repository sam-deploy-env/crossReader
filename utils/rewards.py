from utils import word_generator

def update_rewards(category_repo, runner_repo, setting_repo):
    rewards = get_rewards_in_db(category_repo, runner_repo, setting_repo)
    for reward in rewards:
        category_repo.update(reward)
    if None not in [reward.id for reward in rewards] and setting_repo.get_file_sent() == 0:
        word_generator.create_word_file(category_repo, runner_repo)
        return True
    return False

def get_rewards_in_db(category_repo, runner_repo, setting_repo):
    number_scratch_m = setting_repo.get_number_scratch_m()
    number_scratch_f = setting_repo.get_number_scratch_f()
    rewards = []
    get_rewards_in_scratch(rewards, 'M', number_scratch_m, runner_repo)
    get_rewards_in_scratch(rewards, 'F', number_scratch_f, runner_repo)
    for category in category_repo.get_by_sex('F'):
        get_rewards_in_category(rewards, category.category, 'F', number_scratch_f, runner_repo)
    for category in category_repo.get_by_sex('M'):
        get_rewards_in_category(rewards, category.category, 'M', number_scratch_m, runner_repo)
    ids_rewarded = [reward.id for reward in rewards if reward.id is not None]
    oriol_id_f = runner_repo.get_first_oriol(ids_rewarded, 'F')
    add_runner_in_rewards(rewards, oriol_id_f, "O", 'F')
    oriol_id_m = runner_repo.get_first_oriol(ids_rewarded, 'M')
    add_runner_in_rewards(rewards, oriol_id_m, "O", 'M')
    return rewards

def get_rewards_in_scratch(rewards, sex, number, runner_repo):
    for i in range(1, number+1):
        category = "S" + str(i)
        runner_id = runner_repo.get_reward_in_scratch(i, sex)
        add_runner_in_rewards(rewards, runner_id, category, sex)

def get_rewards_in_category(rewards, category, sex, skip, runner_repo):
    runner_id = runner_repo.get_reward_in_category(category, sex, skip)
    add_runner_in_rewards(rewards, runner_id, category, sex)

def add_runner_in_rewards(rewards, runner_id, category, sex):
    if runner_id:
        reward = RewardInBase(category, sex, runner_id)
    else:
        reward = RewardInBase(category, sex, None)
    rewards.append(reward)

def get_rewards_to_display(category_repo, runner_repo):
    rewards = []
    rewards_in_db = category_repo.get_rewards()
    ids = [reward.runner for reward in rewards_in_db]
    runners = runner_repo.get_rewards_map(ids)
    for reward in rewards_in_db:
        runner = runners.get(reward.runner)
        if runner:
            rewards.append(RewardToDisplay(reward.category, reward.sex, runner.ranking, runner.last_name, runner.first_name, runner.bib_number, runner.get_time()))
        else:
            rewards.append(RewardToDisplay(reward.category, reward.sex))
    return rewards

class RewardInBase:
    
    def __init__(self, category: str, sex: str, id: int = None):
        self.category: str = category
        self.sex: str = sex
        self.id: int = id

class RewardToDisplay:
    
    def __init__(self, category: str, sex: str, ranking: int = None, last_name: str = None, first_name: str = None, bib_number: int = None, time: str = None):
        self.category: str = category
        self.sex: str = sex
        self.ranking: int = ranking
        self.last_name: str = last_name
        self.first_name: str = first_name
        self.bib_number: int = bib_number
        self.time: str = time