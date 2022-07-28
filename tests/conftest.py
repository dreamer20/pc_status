import os
import pytest
from pc_status import create_app
from pc_status.db import init_db, get_db, init_test_data
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

with open(os.path.join(os.path.dirname(__file__), 'schema.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app_with_empty_db(tmpdir):
    db_path = tmpdir.join('database.db')

    app = create_app({'TESTING': True, 'DATABASE': db_path})

    with app.app_context():
        init_db()

    yield app


@pytest.fixture
def app(tmpdir):
    db_path = tmpdir.join('database.db')

    app = create_app({'TESTING': True, 'DATABASE': db_path})

    with app.app_context():
        init_db()
        init_test_data()

    yield app


@pytest.fixture()
def driver():
    opt = Options()
    opt.headless = True
    driver = webdriver.Firefox(options=opt)

    yield driver

    driver.close()


@pytest.fixture
def client(app):
    client = app.test_client()
    return client
