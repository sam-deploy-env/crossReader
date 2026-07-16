from flask import Blueprint, jsonify
from repositories.RunnerRepository import RunnerRepository
from database import SessionLocal

runner_bp = Blueprint("runner_controller", __name__, url_prefix="/runners")

@runner_bp.route("/", methods=["GET"])
def get_runners():
    session = SessionLocal()
    try:
        runner_repo = RunnerRepository(session)
        runners = runner_repo.get_all()
        return jsonify([runner.to_json() for runner in runners])
    finally:
        session.close()