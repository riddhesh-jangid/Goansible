import random
import string
import os
from register import registerObj
import writer

class gcp_compute_instance_group_manager:
    playbook_name = ''
    hosts=[]
    register=[]
    auth_kind = ''
    base_instance_name = ''
    instance_template = ''
    name = ''
    zone = ''
    description = ''
    named_ports = ''
    project = ''
    scopes = ''
    service_account_contents = ''
    service_account_email = ''
    service_account_file = ''
    state = ''
    target_pools = ''
    target_size = ''
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

