import random
import string
import os
from register import registerObj
import writer

class rax_clb_nodes:
    playbook_name = ''
    hosts=[]
    register=[]
    load_balancer_id = ''
    address = ''
    api_key = ''
    auth_endpoint = ''
    condition = ''
    credentials = ''
    env = ''
    identity_type = ''
    node_id = ''
    port = ''
    region = ''
    state = ''
    tenant_id = ''
    tenant_name = ''
    type = ''
    username = ''
    validate_certs = ''
    wait = ''
    wait_timeout = ''
    weight = ''
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

