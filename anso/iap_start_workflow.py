import random
import string
import os
from register import registerObj
import writer

class iap_start_workflow:
    playbook_name = ''
    hosts=[]
    register=[]
    description = ''
    iap_fqdn = ''
    iap_port = ''
    token_key = ''
    variables = ''
    workflow_name = ''
    https = ''
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

