from utils import rewards
from database import SessionLocal

from repositories.RunnerRepository import RunnerRepository
from repositories.CategoryRepository import CategoryRepository

def get_rewards():
    session = SessionLocal()
    try :
        category_repo = CategoryRepository(session)
        runner_repo = RunnerRepository(session)
        return rewards.get_rewards_to_display(category_repo, runner_repo)
    finally:
        session.close()
