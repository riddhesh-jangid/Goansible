import random
import string
import os
from register import registerObj
import writer

class acme_certificate_revoke:
    playbook_name = ''
    hosts=[]
    register=[]
    certificate = ''
    account_key_content = ''
    account_key_src = ''
    account_uri = ''
    acme_directory = ''
    acme_version = ''
    private_key_content = ''
    private_key_src = ''
    revoke_reason = ''
    select_crypto_backend = ''
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

