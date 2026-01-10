import os 


basedir = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.abspath(os.path.join(basedir, '..'))
instance_path = os.path.join(project_root, 'instance')


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my-secret-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Database URL from .env
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    # Configuration for local development
    DEBUG = True
    SQLALCHEMY_ECHO = True #log SQL queries
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(instance_path, 'dev.db')}"

class TestConfig(Config):
    # Configuration for running tests
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(instance_path, 'test.db')}"
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    # Configuration for Production Deployment
    DEBUG = False
    TESTING = False


Config_dict = {
    'development' : DevelopmentConfig,
    'testing' : TestConfig,
    'production' : ProductionConfig
}
