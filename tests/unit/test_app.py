from pc_status import create_app
from pc_status.db_api import get_db


def test_app():
    ''' Checks app testing flag '''
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_db(app):
    """ Returns the same db for app """
    with app.app_context():
        db = get_db()
        assert db is get_db()
