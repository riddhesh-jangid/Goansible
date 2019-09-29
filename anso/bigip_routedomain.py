import random
import string
import os
from register import registerObj
import writer

class bigip_routedomain:
    playbook_name = ''
    hosts=[]
    register=[]
    password = ''
    server = ''
    user = ''
    bwc_policy = ''
    connection_limit = ''
    description = ''
    flow_eviction_policy = ''
    fw_enforced_policy = ''
    id = ''
    name = ''
    parent = ''
    partition = ''
    provider = ''
    routing_protocol = ''
    server_port = ''
    service_policy = ''
    state = ''
    strict = ''
    validate_certs = ''
    vlans = ''
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

