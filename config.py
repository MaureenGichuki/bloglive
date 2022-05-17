import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/blog'
    SECRET_KEY = ('bloglive')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOAD_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


    #email configurations

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'mimowaruguru@gmail.com'
    MAIL_PASSWORD = 'Mangojuice@54'
    SUBJECT_PREFIX = 'BlogsLive'
    SENDER_EMAIL = 'mimowaruguru@gmail.com'

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("://", "ql://",1)

    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/blog'




class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/blog'

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig,

}