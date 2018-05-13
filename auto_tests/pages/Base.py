from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class Base(object):
    def __init__(self, driver):
        self.driver = driver

    def elements(self, locator):
        return self.driver.find_elements(locator.using, locator.selector)

    def element(self, locator):
        return self.driver.find_element(locator.using, locator.selector)

    def click(self):
        self.driver.click()

    def wait_for(self, locator, wait=5):
        return WebDriverWait(self.driver, wait).until(
            EC.visibility_of_element_located((locator.using, locator.selector)))

    def send_keys(self, locator, keys, iframe=False):
        if iframe:
            self.driver = self.driver.parent  # problem when driver has no parent
            frame = self.driver.find_element(By.TAG_NAME, 'iframe')
            self.driver.switch_to.frame(frame)
            self.driver.find_element(locator.using, locator.selector).send_keys(keys)
            self.driver.switch_to.default_content()
        else:
            self.element(locator).send_keys(keys)

    def get_selected(self, locator):
        select = Select(self.element(locator))
        return select.first_selected_option

    def all_selected(self, locator):
        select = Select(self.element(locator))
        return select.all_selected_options

    def select(self, locator, index=None, value=None, text=None):
        select = Select(self.element(locator))
        if index:
            select.select_by_index(index)
        elif value:
            select.select_by_value(value)
        elif text:
            select.select_by_visible_text(text)

    def open_mail_ru(self):
        self.driver.get('https://www.mail.ru')
