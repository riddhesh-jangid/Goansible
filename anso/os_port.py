import random
import string
import os
from register import registerObj
import writer

class os_port:
    playbook_name = ''
    hosts=[]
    register=[]
    network = ''
    admin_state_up = ''
    allowed_address_pairs = ''
    api_timeout = ''
    auth = ''
    auth_type = ''
    availability_zone = ''
    ca_cert = ''
    client_cert = ''
    client_key = ''
    cloud = ''
    device_id = ''
    device_owner = ''
    extra_dhcp_opts = ''
    fixed_ips = ''
    interface = ''
    mac_address = ''
    name = ''
    no_security_groups = ''
    port_security_enabled = ''
    region_name = ''
    security_groups = ''
    state = ''
    timeout = ''
    validate_certs = ''
    vnic_type = ''
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

