import random
import string
import os
from register import registerObj
import writer

class bigip_virtual_address:
    playbook_name = ''
    hosts=[]
    register=[]
    password = ''
    server = ''
    user = ''
    address = ''
    arp = ''
    arp_state = ''
    auto_delete = ''
    availability_calculation = ''
    connection_limit = ''
    icmp_echo = ''
    name = ''
    netmask = ''
    partition = ''
    provider = ''
    route_advertisement = ''
    route_domain = ''
    server_port = ''
    spanning = ''
    state = ''
    traffic_group = ''
    use_route_advertisement = ''
    validate_certs = ''
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

