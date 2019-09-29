import random
import string
import os
from register import registerObj
import writer

class os_ironic:
    playbook_name = ''
    hosts=[]
    register=[]
    driver = ''
    nics = ''
    api_timeout = ''
    auth = ''
    auth_type = ''
    availability_zone = ''
    ca_cert = ''
    chassis_uuid = ''
    client_cert = ''
    client_key = ''
    cloud = ''
    driver_info = ''
    interface = ''
    ironic_url = ''
    name = ''
    properties = ''
    region_name = ''
    skip_update_of_driver_password = ''
    state = ''
    timeout = ''
    uuid = ''
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

