from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

db = SQLAlchemy()

engine = create_engine(os.getenv('DATABASE_URL'), future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)