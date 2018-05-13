from selenium.webdriver.common.by import By
from auto_tests.locators.Locator import Locator

MAILBOX = Locator(By.ID, 'mailbox-container')
LOGIN = Locator(By.ID, 'mailbox:login')
PASSWORD = Locator(By.ID, 'mailbox:password')
DOMAIN = Locator(By.ID, 'mailbox:domain')
MAIL_SUBMIT = Locator(By.ID, 'mailbox:submit')
