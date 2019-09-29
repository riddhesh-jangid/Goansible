import random
import string
import os
from register import registerObj
import writer

class cs_network_offering:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    api_http_method = ''
    api_key = ''
    api_region = ''
    api_secret = ''
    api_timeout = ''
    api_url = ''
    availability = ''
    conserve_mode = ''
    details = ''
    display_text = ''
    egress_default_policy = ''
    for_vpc = ''
    guest_ip_type = ''
    keepalive_enabled = ''
    max_connections = ''
    network_rate = ''
    persistent = ''
    service_capabilities = ''
    service_offering = ''
    service_providers = ''
    specify_ip_ranges = ''
    specify_vlan = ''
    state = ''
    supported_services = ''
    traffic_type = ''
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

