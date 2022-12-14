import os
import pytest
from pc_status import create_app
from pc_status.db import init_db, init_test_data
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

SELENIUM_GRID_HOST = os.getenv('SELENIUM_GRID_HOST')
SELENIUM_GRID_PORT = os.getenv('SELENIUM_GRID_PORT', default='4444')
APP_HOST = os.getenv('APP_HOST', default='localhost')
APP_PORT = os.getenv('APP_PORT', default='8000')


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
    if SELENIUM_GRID_HOST is not None:
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Remote(
            command_executor=f'http://{SELENIUM_GRID_HOST}:{SELENIUM_GRID_PORT}',
            options=chrome_options
        )
    else:
        opt = Options()
        opt.headless = True
        driver = webdriver.Firefox(options=opt)

    yield driver

    driver.quit()


@pytest.fixture()
def app_root_url():
    return f'http://{APP_HOST}:{APP_PORT}'


@pytest.fixture
def client(app):
    client = app.test_client()
    return client


@pytest.fixture
def client_empty_db(app_with_empty_db):
    client = app_with_empty_db.test_client()
    return client
