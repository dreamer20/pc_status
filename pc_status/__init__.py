import os
from datetime import datetime
from flask import Flask
from config import Config

def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_object(Config)

    if test_config is not None:
        app.config.from_mapping(test_config)


    @app.template_filter('valueformat')
    def valueformat_filter(value):
        if value == '':
            return '-'
        return value


    @app.template_filter('fromtimestamp')
    def fromtimestamp_filter(timestamp):
        return datetime.fromtimestamp(timestamp).strftime("%Y.%m.%d %H:%M")


    @app.template_filter('uptimeformat')
    def uptimeformat_filter(time):
        if len(time) in (1, 2):
            return f'{time} мин.'
        elif len(time) > 2:
            _time = time.replace(':', ' ч. ')
            return f'{_time} мин.'
        else:
            return '-'


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