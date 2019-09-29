import random
import string
import os
from register import registerObj
import writer

class rax_clb_ssl:
    playbook_name = ''
    hosts=[]
    register=[]
    loadbalancer = ''
    api_key = ''
    auth_endpoint = ''
    certificate = ''
    credentials = ''
    enabled = ''
    env = ''
    https_redirect = ''
    identity_type = ''
    intermediate_certificate = ''
    private_key = ''
    region = ''
    secure_port = ''
    secure_traffic_only = ''
    state = ''
    tenant_id = ''
    tenant_name = ''
    username = ''
    validate_certs = ''
    wait = ''
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

