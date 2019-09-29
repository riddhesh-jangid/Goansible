import random
import string
import os
from register import registerObj
import writer

class bigip_gtm_server:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    availability_requirements = ''
    datacenter = ''
    devices = ''
    iquery_options = ''
    limits = ''
    link_discovery = ''
    monitors = ''
    partition = ''
    prober_fallback = ''
    prober_pool = ''
    prober_preference = ''
    provider = ''
    server_port = ''
    server_type = ''
    state = ''
    validate_certs = ''
    virtual_server_discovery = ''
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

