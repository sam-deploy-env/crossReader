
from flask import Blueprint, jsonify
from repositories.SettingRepository import SettingRepository
from database import SessionLocal

setting_bp = Blueprint("setting_controller", __name__, url_prefix="/settings")

@setting_bp.route("/started", methods=["GET"])
def get_started():
    session = SessionLocal()
    try:
        setting_repo = SettingRepository(session)
        return jsonify(setting_repo.get_started())
    finally:
        session.close()