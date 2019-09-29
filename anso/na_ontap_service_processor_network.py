import random
import string
import os
from register import registerObj
import writer

class na_ontap_service_processor_network:
    playbook_name = ''
    hosts=[]
    register=[]
    address_type = ''
    hostname = ''
    is_enabled = ''
    node = ''
    password = ''
    username = ''
    dhcp = ''
    gateway_ip_address = ''
    http_port = ''
    https = ''
    ip_address = ''
    netmask = ''
    ontapi = ''
    prefix_length = ''
    state = ''
    validate_certs = ''
    wait_for_completion = ''
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

