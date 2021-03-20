import os

class Config(object):
    SECRET_KEY = os.environ.get('CHAVE_SECRETA')    

