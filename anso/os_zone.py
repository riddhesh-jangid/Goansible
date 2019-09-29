import random
import string
import os
from register import registerObj
import writer

class os_zone:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    api_timeout = ''
    auth = ''
    auth_type = ''
    availability_zone = ''
    ca_cert = ''
    client_cert = ''
    client_key = ''
    cloud = ''
    description = ''
    email = ''
    interface = ''
    masters = ''
    region_name = ''
    state = ''
    timeout = ''
    ttl = ''
    validate_certs = ''
    wait = ''
    zone_type = ''
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

