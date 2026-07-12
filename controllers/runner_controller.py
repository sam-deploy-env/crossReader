from flask import Blueprint, jsonify
from repositories.RunnerRepository import RunnerRepository

runner_repository = RunnerRepository()

runner_bp = Blueprint("runner_controller", __name__, url_prefix="/runners")

@runner_bp.route("/", methods=["GET"])
def get_runners():
    runners = runner_repository.get_all()
    return jsonify([runner.to_json() for runner in runners])