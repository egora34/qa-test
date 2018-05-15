from selenium.webdriver.common.by import By
from auto_tests.locators.Locator import Locator

LEGO = Locator(By.ID, 'LEGO')
IFRAME = Locator(By.TAG_NAME, 'iframe')

MAILBOX_HEADER = Locator(By.CLASS_NAME, 'b-sticky')
NEW_MAIL_CREATE = Locator(By.CLASS_NAME, 'ico_toolbar_compose')

MAIL_DELETE = Locator(By.CLASS_NAME, 'ico_toolbar_remove')
MAIL_ARCHIVE = Locator(By.CLASS_NAME, 'ico_toolbar_archive')

SEND_MAIL = Locator(By.CSS_SELECTOR, '[data-name=send]')

MAILBOX_FOLDERS = Locator(By.ID, 'b-nav_folders')
SENT = Locator(By.CLASS_NAME, 'ico_folder_send')

LETTERS = Locator(By.ID, 'b-letters')
SENT_LETTERS = Locator(By.CLASS_NAME, 'b-datalist_letters_to')

LETTER = Locator(By.CLASS_NAME, 'b-datalist__item')
LETTER_SUBJECT = Locator(By.CLASS_NAME, 'b-datalist__item__subj')
LETTER_BODY = Locator(By.CLASS_NAME, 'b-datalist__item__subj__snippet')

NEW_MAIL_CONTAINER = Locator(By.ID, 'b-compose')

NEW_SENT_TO = Locator(By.CSS_SELECTOR, '[data-original-name="To"]')
NEW_SUBJECT = Locator(By.CSS_SELECTOR, '[name=Subject]')
NEW_BODY = Locator(By.ID, 'tinymce')

SUCCESS_MESSAGE = Locator(By.CLASS_NAME, 'message-sent_IsSocialConnect')
