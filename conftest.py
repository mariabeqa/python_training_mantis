from fixture.application import Application

import pytest
import json
import os.path
from fixture.db import DbFixture
from generator import test_data_generator

from model.project import Project

fixture=None
target=None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture(scope="session", autouse=True)
def config(request):
    return load_config(request.config.getoption("--target"))

@pytest.fixture()
def app(request, config):
    global fixture
    global target

    browser = request.config.getoption("--browser")
    web_config = config

    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, config=config)
        fixture.session.ensure_login(username=web_config['webAdmin']['username'], password=web_config['webAdmin']['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture
def gen_project():
    return Project(
        name=test_data_generator.get_project_name(),
        description=test_data_generator.get_project_description()
    )


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "target.json")
    parser.addoption("--targetPath", action="store", default=config_file)

