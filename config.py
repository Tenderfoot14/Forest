import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'shh! it\'s a secret!'
    COLOR = 'blue'
    NAME = 'The Forest'
    MONGOALCHEMY_DATABASE = 'heroku_d09c40b5'
    MONGOALCHEMY_CONNECTION_STRING = os.eviron.get('MONGOLAB_URI')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


class HerokuConfig(ProductionConfig):
    @classmethod
    def init_app(app):
        ProductionConfig.init_app(app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
