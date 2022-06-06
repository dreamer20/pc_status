import tempfile, os, pytest
from pc_status import create_app
from pc_status.db import init_db, get_db


with open(os.path.join(os.path.dirname(__file__), 'schema.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app(tmpdir):
    db_path = tmpdir.join('database.db')

    app = create_app({'TESTING': True, 'DATABASE': db_path})

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app


@pytest.fixture
def client(app):
    client = app.test_client()
    return client