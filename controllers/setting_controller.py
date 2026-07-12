
from flask import Blueprint, jsonify
from repositories.SettingRepository import SettingRepository

setting_repository = SettingRepository()

setting_bp = Blueprint("setting_controller", __name__, url_prefix="/settings")

@setting_bp.route("/started", methods=["GET"])
def get_started():
    return jsonify(setting_repository.get_started())