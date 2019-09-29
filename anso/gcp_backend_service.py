import random
import string
import os
from register import registerObj
import writer

class gcp_backend_service:
    playbook_name = ''
    hosts=[]
    register=[]
    backend_service_name = ''
    backends = ''
    healthchecks = ''
    credentials_file = ''
    enable_cdn = ''
    port_name = ''
    project_id = ''
    protocol = ''
    service_account_email = ''
    state = ''
    timeout = ''
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

