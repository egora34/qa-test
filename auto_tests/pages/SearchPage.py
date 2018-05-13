from auto_tests.pages.Base import *
from auto_tests.locators.SearchPage import *


class SearchPage(Base):
    @property
    def get_mailbox_container(self):
        return MailboxContainer(Base.element(self, MAILBOX))


class MailboxContainer(Base):
    def input_login(self, login):
        Base.send_keys(self, LOGIN, login)

    def input_password(self, password):
        Base.send_keys(self, PASSWORD, password)

    def select_domain(self, domain):
        if Base.get_selected(self, DOMAIN) != domain:
            Base.select(self, DOMAIN, text=domain)

    def login(self, login, domain, password):
        self.input_login(login)
        self.input_password(password)
        self.select_domain(domain)
        Base.element(self, MAIL_SUBMIT).click()