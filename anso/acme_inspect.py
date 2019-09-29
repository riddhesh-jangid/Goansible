import random
import string
import os
from register import registerObj
import writer

class acme_inspect:
    playbook_name = ''
    hosts=[]
    register=[]
    account_key_content = ''
    account_key_src = ''
    account_uri = ''
    acme_directory = ''
    acme_version = ''
    content = ''
    fail_on_acme_error = ''
    method = ''
    select_crypto_backend = ''
    url = ''
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

