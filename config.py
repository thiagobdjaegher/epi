import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:

    SECRET_KEY = os.environ.get('KEY')

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_BINDS = {
        'sgh': os.environ.get('SGH_DATABASE_URI')
    }
    SQLALCHEMY_ECHO = os.environ.get('SQLALCHEMY_ECHO')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
