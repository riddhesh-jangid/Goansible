import random
import string
import os
from register import registerObj
import writer

class ovirt_external_provider:
    playbook_name = ''
    hosts=[]
    register=[]
    auth = ''
    authentication_keys = ''
    authentication_url = ''
    data_center = ''
    description = ''
    fetch_nested = ''
    name = ''
    nested_attributes = ''
    network_type = ''
    password = ''
    poll_interval = ''
    read_only = ''
    state = ''
    tenant_name = ''
    timeout = ''
    type = ''
    url = ''
    username = ''
    wait = ''
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

