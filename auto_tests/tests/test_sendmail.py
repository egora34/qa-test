import pytest
from auto_tests.pages.SearchPage import SearchPage
from auto_tests.pages.Mailbox import Mailbox
import random
import string


class TestSendMail(object):
    subject = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    @pytest.mark.parametrize("email,password", [('qa_test_test@mail.ru', 'f8Jka^y')])
    def test_login(self, email, password):
        SearchPage.open_mail_ru(self)

        # just trust income data without checking if it is valid
        email = email.split('@')
        login = email[0]
        domain = '@' + email[1]

        # get mailbox container to work only with it
        search_page = SearchPage(self.driver)
        mailbox_container = search_page.get_mailbox_container
        mailbox_container.login(login=login, domain=domain, password=password)

        # to assert that login was correct wait for loading main container at mailbox
        print('somethiong')
        assert Mailbox.wait_for_mailbox(self)

    @pytest.mark.parametrize("email, body", [('qa_test_test@mail.ru', 'lorem ipsum etc')])
    def test_send_mail(self, email, body):
        mailbox_page = Mailbox(self.driver)
        header = mailbox_page.mailbox_header
        header.create_new_mail()
        mailbox_page.wait_for_iframe()

        new_mail = mailbox_page.new_mail_container
        header = mailbox_page.mailbox_header

        new_mail.input_email_to(email)
        new_mail.input_subject(self.subject)
        new_mail.input_body(body)

        header.send_mail()

        assert new_mail.wait_for_success_message()

    def test_new_sent_mail(self):
        mailbox_page = Mailbox(self.driver)
        folders = mailbox_page.folders
        folders.open_sent()

        mailbox_page.wait_for_letters()
        letters = mailbox_page.letters
        sent_messages = letters.all_letters()
        subjects = [i.subject for i in sent_messages]
        assert self.subject in subjects
