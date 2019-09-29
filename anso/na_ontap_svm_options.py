import random
import string
import os
from register import registerObj
import writer

class na_ontap_svm_options:
    playbook_name = ''
    hosts=[]
    register=[]
    hostname = ''
    password = ''
    username = ''
    vserver = ''
    http_port = ''
    https = ''
    name = ''
    ontapi = ''
    validate_certs = ''
    value = ''
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

