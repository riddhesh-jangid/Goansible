import random
import string
import os
from register import registerObj
import writer

class dimensiondata_vlan:
    playbook_name = ''
    hosts=[]
    register=[]
    location = ''
    network_domain = ''
    allow_expand = ''
    description = ''
    mcp_password = ''
    mcp_user = ''
    name = ''
    private_ipv4_base_address = ''
    private_ipv4_prefix_size = ''
    region = ''
    state = ''
    validate_certs = ''
    wait = ''
    wait_poll_interval = ''
    wait_time = ''
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

