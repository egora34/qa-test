from auto_tests.pages.Base import *
from auto_tests.locators.Mailbox import *


class Mailbox(Base):
    def wait_for_mailbox(self):
        return Base.wait_for(self, NEW_MAIL_CREATE, wait=10)

    @property
    def mailbox_header(self):
        return MailboxHeader(Base.element(self, MAILBOX_HEADER))

    @property
    def new_mail_container(self):
        return NewMailContainer(Base.element(self, NEW_MAIL_CONTAINER))

    def wait_for_iframe(self):
        return Base.wait_for(self, IFRAME)

    def wait_for_letters(self):
        Base.wait_for(self, LETTERS)

    @property
    def folders(self):
        return MailboxFolders(Base.element(self, MAILBOX_FOLDERS))

    @property
    def letters(self):
        return Letters(Base.element(self, SENT_LETTERS))


class Letters(Base):
    def all_letters(self):
        return [Letter(i) for i in Base.elements(self, LETTER)]


class MailboxFolders(Base):
    def open_sent(self):
        Base.element(self, SENT).click()


class Letter(Base):
    @property
    def subject(self):
        subj = Base.element(self, LETTER_SUBJECT).text
        subj = subj.replace(Base.element(self, LETTER_BODY).text, '')
        return subj


class MailboxHeader(Base):
    def create_new_mail(self):
        Base.element(self, NEW_MAIL_CREATE).click()

    def send_mail(self):
        Base.element(self, SEND_MAIL).click()


class NewMailContainer(Base):
    def input_email_to(self, email):
        Base.send_keys(self, NEW_SENT_TO, email)

    def input_subject(self, subject):
        Base.send_keys(self, NEW_SUBJECT, subject)

    def input_body(self, body):
        Base.send_keys(self, NEW_BODY, body, iframe=True)

    def wait_for_success_message(self):
        return Base.wait_for(self, SUCCESS_MESSAGE)
