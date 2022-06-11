import os

from flask import Flask
from config import Config

def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_object(Config)

    if test_config is not None:
        app.config.from_mapping(test_config)

    from . import main, search
    app.register_blueprint(main.bp)
    app.register_blueprint(search.bp)

    from . import db
    db.init_app(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app