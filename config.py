import os

class Config:
    
    '''
    Describes the general configurations
    '''
    SECRET_KEY = os.urandom(32)
    # app.config['SECRET_KEY'] = 'bEtteR23'
    
    DATABASE_PASS = os.environ.get('DATABASE_PASS')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    #emails configuration
    
    MAIL_SERVER=os.environ.get('MAIL_SERVER')
    MAIL_PORT=os.environ.get('MAIL_PORT')
    MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    
    
    
    #Simple MDE configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
    @staticmethod
    def init_app(app):
        pass
    
   
  
    
    
class ProdConfig(Config):
    
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    
    
    
class DevConfig(Config):

    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
        
    '''
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 
    
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://brian:brayo13@localhost/pitch'
    
    DEBUG = True
    
class TestConfig(Config):
    
    '''
    Test configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    
    DATABASE_PASS = os.environ.get('DATABASE_PASS')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://brian:brayo13@localhost/pitch'
    
    
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test': TestConfig
}
        
    