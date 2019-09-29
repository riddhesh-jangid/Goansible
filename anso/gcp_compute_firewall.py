import random
import string
import os
from register import registerObj
import writer

class gcp_compute_firewall:
    playbook_name = ''
    hosts=[]
    register=[]
    auth_kind = ''
    name = ''
    allowed = ''
    denied = ''
    description = ''
    destination_ranges = ''
    direction = ''
    disabled = ''
    network = ''
    priority = ''
    project = ''
    scopes = ''
    service_account_contents = ''
    service_account_email = ''
    service_account_file = ''
    source_ranges = ''
    source_service_accounts = ''
    source_tags = ''
    state = ''
    target_service_accounts = ''
    target_tags = ''
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

