import random
import string
import os
from register import registerObj
import writer

class cs_vlan_ip_range:
    playbook_name = ''
    hosts=[]
    register=[]
    start_ip = ''
    account = ''
    api_http_method = ''
    api_key = ''
    api_region = ''
    api_secret = ''
    api_timeout = ''
    api_url = ''
    cidr_ipv6 = ''
    domain = ''
    end_ip = ''
    end_ipv6 = ''
    for_virtual_network = ''
    gateway = ''
    gateway_ipv6 = ''
    netmask = ''
    network = ''
    physical_network = ''
    project = ''
    start_ipv6 = ''
    state = ''
    vlan = ''
    zone = ''
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

