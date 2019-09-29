import random
import string
import os
from register import registerObj
import writer

class vca_nat:
    playbook_name = ''
    hosts=[]
    register=[]
    nat_rules = ''
    api_version = ''
    gateway_name = ''
    host = ''
    instance_id = ''
    org = ''
    password = ''
    purge_rules = ''
    service_type = ''
    state = ''
    username = ''
    validate_certs = ''
    vdc_name = ''
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

