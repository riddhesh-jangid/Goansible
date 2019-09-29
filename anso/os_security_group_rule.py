import random
import string
import os
from register import registerObj
import writer

class os_security_group_rule:
    playbook_name = ''
    hosts=[]
    register=[]
    security_group = ''
    api_timeout = ''
    auth = ''
    auth_type = ''
    availability_zone = ''
    ca_cert = ''
    client_cert = ''
    client_key = ''
    cloud = ''
    direction = ''
    ethertype = ''
    interface = ''
    port_range_max = ''
    port_range_min = ''
    project = ''
    protocol = ''
    region_name = ''
    remote_group = ''
    remote_ip_prefix = ''
    state = ''
    timeout = ''
    validate_certs = ''
    wait = ''
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

