import random
import string
import os
from register import registerObj
import writer

class na_elementsw_network_interfaces:
    playbook_name = ''
    hosts=[]
    register=[]
    gateway_address_10g = ''
    gateway_address_1g = ''
    hostname = ''
    ip_address_10g = ''
    ip_address_1g = ''
    method = ''
    password = ''
    subnet_10g = ''
    subnet_1g = ''
    username = ''
    bond_mode_10g = ''
    bond_mode_1g = ''
    dns_nameservers = ''
    dns_search_domains = ''
    lacp_10g = ''
    lacp_1g = ''
    mtu_10g = ''
    mtu_1g = ''
    virtual_network_tag = ''
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

