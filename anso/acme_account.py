import random
import string
import os
from register import registerObj
import writer

class acme_account:
    playbook_name = ''
    hosts=[]
    register=[]
    state = ''
    account_key_content = ''
    account_key_src = ''
    account_uri = ''
    acme_directory = ''
    acme_version = ''
    allow_creation = ''
    contact = ''
    new_account_key_content = ''
    new_account_key_src = ''
    select_crypto_backend = ''
    terms_agreed = ''
    validate_certs = ''
    def compile(self):
       self.playbook_name=writer.writer(self,self.playbook_name)

    def run(self):
       dump_name=''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
       os.system('{} | tee {}'.format(self.playbook_name,dump_name))
       self.register = registerObj(dump_name)
       os.remove(dump_name)

    def go(self):
       self.compile()
       self.run()

