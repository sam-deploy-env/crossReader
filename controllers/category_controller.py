
from flask import Blueprint, jsonify

from repositories.CategoryRepository import CategoryRepository
from repositories.RunnerRepository import RunnerRepository
from database import SessionLocal
from utils import rewards

category_bp = Blueprint("category_controller", __name__, url_prefix="/categories")

@category_bp.route("/", methods=["GET"])
def get_categories():
    session = SessionLocal()
    try:
        category_repo = CategoryRepository(session)
        categories = category_repo.get_no_scratch_no_oriol()
        return jsonify([category.to_json() for category in categories])
    finally:
        session.close()

@category_bp.route("/rewards", methods=["GET"])
def get_rewards():
    session = SessionLocal()
    try:
        category_repo = CategoryRepository(session)
        runner_repo = RunnerRepository(session)
        rewards_to_display = rewards.get_rewards_to_display(category_repo, runner_repo)
        return jsonify([reward.__dict__ for reward in rewards_to_display])
    finally:
        session.close()