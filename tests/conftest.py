import random

import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture()
def phone():
    return f"+7{random.randint(1000000000, 9999999999)}"