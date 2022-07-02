import os
from flask import Flask
from config import Config
from .filters import valueformat, fromtimestamp, uptimeformat


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_object(Config)

    app.jinja_env.filters['valueformat'] = valueformat
    app.jinja_env.filters['fromtimestamp'] = fromtimestamp
    app.jinja_env.filters['uptimeformat'] = uptimeformat

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
