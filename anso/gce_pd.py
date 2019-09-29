import random
import string
import os
from register import registerObj
import writer

class gce_pd:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    credentials_file = ''
    delete_on_termination = ''
    detach_only = ''
    disk_type = ''
    image = ''
    instance_name = ''
    mode = ''
    pem_file = ''
    project_id = ''
    service_account_email = ''
    size_gb = ''
    snapshot = ''
    state = ''
    zone = ''
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

