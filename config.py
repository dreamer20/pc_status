import os
from werkzeug.security import generate_password_hash

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = generate_password_hash('my-secret-key')
    DATABASE = os.path.join(basedir, 'database.db')