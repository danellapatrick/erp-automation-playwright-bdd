import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pytest
from pages.login_page import LoginPage
from pages.farmers_page import FarmersPage


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def farmers_page(page):
    return FarmersPage(page)