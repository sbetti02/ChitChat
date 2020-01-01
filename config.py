import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'ScottMessager.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'ScottMessager.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
