import random
import string
import os
from register import registerObj
import writer

class java_cert:
    playbook_name = ''
    hosts=[]
    register=[]
    keystore_pass = ''
    cert_alias = ''
    cert_path = ''
    cert_port = ''
    cert_url = ''
    executable = ''
    keystore_create = ''
    keystore_path = ''
    keystore_type = ''
    pkcs12_alias = ''
    pkcs12_password = ''
    pkcs12_path = ''
    state = ''
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

