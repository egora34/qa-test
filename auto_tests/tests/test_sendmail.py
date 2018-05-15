import pytest
from auto_tests.pages.SearchPage import SearchPage
from auto_tests.pages.Mailbox import Mailbox
import random
import string

class TestSendMail(object):

 # need to parametrize test data
    subject = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    email = 'qa_test_test@mail.ru'
    password = 'f8Jka^y'
    body = 'lorem ipsum etc'
    
    def test_login(self):
        SearchPage.open_mail_ru(self)
        
        # just trust income data without checking if it is valid
        email = self.email.split('@')
        login = email[0]
        domain = '@' + email[1]
        password = self.password
        
        # get mailbox container to work only with it
        search_page = SearchPage(self.driver)
        mailbox_container = search_page.get_mailbox_container
        mailbox_container.login(login=login, domain=domain, password=password)
        
        # to assert that login was correct wait for loading main container at mailbox
        assert Mailbox.wait_for_mailbox(self)
        
    def test_send_mail(self):
        mailbox_page = Mailbox(self.driver)
        header = mailbox_page.mailbox_header
        header.create_new_mail()
        mailbox_page.wait_for_iframe()
        
        new_mail = mailbox_page.new_mail_container
        header = mailbox_page.mailbox_header
            
        new_mail.input_email_to(self.email)
        new_mail.input_subject(self.subject)
        new_mail.input_body(self.body)
            
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
