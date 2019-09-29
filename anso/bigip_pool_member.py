import random
import string
import os
from register import registerObj
import writer

class bigip_pool_member:
    playbook_name = ''
    hosts=[]
    register=[]
    password = ''
    pool = ''
    port = ''
    server = ''
    state = ''
    user = ''
    address = ''
    aggregate = ''
    availability_requirements = ''
    connection_limit = ''
    description = ''
    fqdn = ''
    fqdn_auto_populate = ''
    ip_encapsulation = ''
    monitors = ''
    name = ''
    partition = ''
    preserve_node = ''
    priority_group = ''
    provider = ''
    rate_limit = ''
    ratio = ''
    replace_all_with = ''
    reuse_nodes = ''
    server_port = ''
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

