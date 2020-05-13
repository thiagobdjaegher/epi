import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:

    SECRET_KEY = os.environ.get('S_KEY')

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DF_DB_URI')
    SQLALCHEMY_BINDS = {
        'sgh': os.environ.get('SGH_DB_URI')
    }
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
