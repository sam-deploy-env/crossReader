
from flask import Blueprint, jsonify
from repositories.CategoryRepository import CategoryRepository
from business import category_business

category_repository = CategoryRepository()

category_bp = Blueprint("category_controller", __name__, url_prefix="/categories")

@category_bp.route("/", methods=["GET"])
def get_categories():
    categories = category_repository.get_no_scratch_no_oriol()
    return jsonify([category.to_json() for category in categories])

@category_bp.route("/rewards", methods=["GET"])
def get_rewards():
    rewards = category_business.get_rewards()
    return jsonify([reward.__dict__ for reward in rewards])