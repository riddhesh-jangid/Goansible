import random
import string
import os
from register import registerObj
import writer

class bigip_tunnel:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    auto_last_hop = ''
    description = ''
    key = ''
    local_address = ''
    mode = ''
    mtu = ''
    partition = ''
    profile = ''
    provider = ''
    remote_address = ''
    secondary_address = ''
    server_port = ''
    state = ''
    tos = ''
    traffic_group = ''
    transparent = ''
    use_pmtu = ''
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

