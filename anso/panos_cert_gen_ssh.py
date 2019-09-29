import random
import string
import os
from register import registerObj
import writer

class panos_cert_gen_ssh:
    playbook_name = ''
    hosts=[]
    register=[]
    cert_cn = ''
    cert_friendly_name = ''
    ip_address = ''
    key_filename = ''
    password = ''
    signed_by = ''
    rsa_nbits = ''
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

