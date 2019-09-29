import random
import string
import os
from register import registerObj
import writer

class os_subnet:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    allocation_pool_end = ''
    allocation_pool_start = ''
    api_timeout = ''
    auth = ''
    auth_type = ''
    availability_zone = ''
    ca_cert = ''
    cidr = ''
    client_cert = ''
    client_key = ''
    cloud = ''
    dns_nameservers = ''
    enable_dhcp = ''
    extra_specs = ''
    gateway_ip = ''
    host_routes = ''
    interface = ''
    ip_version = ''
    ipv6_address_mode = ''
    ipv6_ra_mode = ''
    network_name = ''
    no_gateway_ip = ''
    project = ''
    region_name = ''
    state = ''
    timeout = ''
    use_default_subnetpool = ''
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

