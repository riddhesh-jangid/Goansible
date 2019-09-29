import random
import string
import os
from register import registerObj
import writer

class openssl_pkcs12:
    playbook_name = ''
    hosts=[]
    register=[]
    path = ''
    action = ''
    attributes = ''
    backup = ''
    certificate_path = ''
    force = ''
    friendly_name = ''
    group = ''
    iter_size = ''
    maciter_size = ''
    mode = ''
    other_certificates = ''
    owner = ''
    passphrase = ''
    privatekey_passphrase = ''
    privatekey_path = ''
    selevel = ''
    serole = ''
    setype = ''
    seuser = ''
    src = ''
    state = ''
    unsafe_writes = ''
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

