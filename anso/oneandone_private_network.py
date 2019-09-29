import random
import string
import os
from register import registerObj
import writer

class oneandone_private_network:
    playbook_name = ''
    hosts=[]
    register=[]
    auth_token = ''
    name = ''
    private_network = ''
    add_members = ''
    api_url = ''
    datacenter = ''
    description = ''
    network_address = ''
    remove_members = ''
    state = ''
    subnet_mask = ''
    wait = ''
    wait_interval = ''
    wait_timeout = ''
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

