from flask import Blueprint, jsonify, request
from config.config import DISCORD_WEBHOOK_URL
from utils.discord_webhook import send_discord_message
from flask import current_app

comment_bp = Blueprint("comment_controller", __name__, url_prefix="/comments")

@comment_bp.route("/", methods=["POST"])
def create_comment():
    data = request.get_json()
    
    if not data or 'name' not in data or 'comment' not in data:
        return jsonify({"error": "Le nom et le commentaire sont requis"}), 400
    
    if DISCORD_WEBHOOK_URL:
        success = send_discord_message(
            webhook_url=DISCORD_WEBHOOK_URL,
            name=data['name'],
            comment=data['comment']
        )
        if not success:
            current_app.logger.error("Échec de l'envoi du commentaire vers Discord")
    
    return jsonify({"message": "Commentaire reçu avec succès"}), 201