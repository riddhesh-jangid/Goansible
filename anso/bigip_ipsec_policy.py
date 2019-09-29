import random
import string
import os
from register import registerObj
import writer

class bigip_ipsec_policy:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    auth_algorithm = ''
    description = ''
    encrypt_algorithm = ''
    ipcomp = ''
    kb_lifetime = ''
    lifetime = ''
    mode = ''
    partition = ''
    perfect_forward_secrecy = ''
    protocol = ''
    provider = ''
    route_domain = ''
    server_port = ''
    state = ''
    tunnel_local_address = ''
    tunnel_remote_address = ''
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

