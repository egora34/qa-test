import pytest
import time
from selenium import webdriver
import csv

driver = webdriver.Chrome()

# def pytest_addoption(parser):
# parser.addoption("--file", action="append", default=None)

# def pytest_generate_tests(metafunc):
# 

@pytest.fixture(scope="class", autouse=True)
def resource_a_setup(request):
    driver.maximize_window()
    request.cls.driver = driver
    
    def resource_a_teardown():
        time.sleep(1)
        driver.quit()
        
    request.addfinalizer(resource_a_teardown)
