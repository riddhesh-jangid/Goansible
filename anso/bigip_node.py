import random
import string
import os
from register import registerObj
import writer

class bigip_node:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    address = ''
    availability_requirements = ''
    connection_limit = ''
    description = ''
    dynamic_ratio = ''
    fqdn = ''
    fqdn_address_type = ''
    fqdn_auto_populate = ''
    fqdn_down_interval = ''
    fqdn_up_interval = ''
    monitor_type = ''
    monitors = ''
    partition = ''
    provider = ''
    quorum = ''
    rate_limit = ''
    ratio = ''
    server_port = ''
    state = ''
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

