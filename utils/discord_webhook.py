import requests
import json
import datetime
from flask import current_app

def send_discord_message(webhook_url: str, name: str, comment: str) -> bool:
    if not webhook_url:
        current_app.logger.warning("Aucune URL de webhook Discord configurée")
        return False
        
    data = {
        "embeds": [{
            "title": "Commentaire de " + name,
            "description": comment,
            "color": 0x00ff88,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
        }]
    }
    
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(
            webhook_url,
            data=json.dumps(data),
            headers=headers
        )
        response.raise_for_status()
        return True
    except Exception as e:
        current_app.logger.error(f"Erreur lors de l'envoi du message Discord: {str(e)}")
        return False
