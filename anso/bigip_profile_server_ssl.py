import random
import string
import os
from register import registerObj
import writer

class bigip_profile_server_ssl:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    certificate = ''
    chain = ''
    ciphers = ''
    key = ''
    ocsp_profile = ''
    parent = ''
    partition = ''
    passphrase = ''
    provider = ''
    secure_renegotiation = ''
    server_certificate = ''
    server_name = ''
    server_port = ''
    sni_default = ''
    sni_require = ''
    state = ''
    update_password = ''
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

