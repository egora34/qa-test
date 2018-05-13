import pytest
import time
from selenium import webdriver

driver = webdriver.Chrome()

@pytest.fixture(scope="class", autouse=True)
def resource_a_setup(request):
    driver.maximize_window()
    request.cls.driver = driver

    def resource_a_teardown():
        time.sleep(1)
        driver.quit()

    request.addfinalizer(resource_a_teardown)
