import random
import string
import os
from register import registerObj
import writer

class os_nova_flavor:
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
    disk = ''
    ephemeral = ''
    extra_specs = ''
    flavorid = ''
    interface = ''
    is_public = ''
    ram = ''
    region_name = ''
    rxtx_factor = ''
    state = ''
    swap = ''
    timeout = ''
    validate_certs = ''
    vcpus = ''
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

