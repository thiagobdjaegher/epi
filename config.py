class Config:

    SECRET_KEY = 'igh@2020'
    FLASK_APP = 'wsgi.py'
    FLASK_DEBUG = 1

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db_file/epi.db'
    SQLALCHEMY_BINDS = {
        'sgh': 'firebird://sysdba:masterkey@192.168.135.245:3050//banco/sghdados.1925'
    }
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
