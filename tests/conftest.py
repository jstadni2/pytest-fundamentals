import pytest

from demos.db import create_engine, setup_db, teardown_db


class WebDriver:
    def login(self, user):
        # Code to log in as user...
        html = f"<html>Welcome {user['first_name']} {user['last_name']}!</html>"
        return html


@pytest.fixture()
def webdriver():
    return WebDriver()


@pytest.fixture(scope='function')
def db_connection():
    """Connection to an empty database"""
    
    test_engine = create_engine()
    setup_db(test_engine)
    connection = test_engine.connect()
    yield connection
    connection.close()
    teardown_db(test_engine)


@pytest.fixture(scope='session')
def db_connection_test_data(db_connection):
    """Connection to a database prepopulated with test data"""
    
    db_connection.execute('test_data.sql')
    return db_connection
