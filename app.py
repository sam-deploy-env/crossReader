from flask_cors import CORS
from flask import Flask
import threading

from controllers.category_controller import category_bp
from controllers.comment_controller import comment_bp
from controllers.setting_controller import setting_bp
from controllers.runner_controller import runner_bp
from controllers import discord_controller

from config.Dbconfig import Dbconfig
from database import db

app = Flask(__name__)
CORS(app)

app.config.from_object(Dbconfig)
db.init_app(app)

app.register_blueprint(category_bp)
app.register_blueprint(comment_bp)
app.register_blueprint(setting_bp)
app.register_blueprint(runner_bp)


def run_discord_bot():
    with app.app_context():
        discord_controller.main()

#Création des tables
with app.app_context():
    db.create_all()

discordThread = threading.Thread(target=run_discord_bot)
discordThread.start()

if __name__ == '__main__':
    app.run()