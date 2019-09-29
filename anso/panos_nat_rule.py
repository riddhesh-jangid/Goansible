import random
import string
import os
from register import registerObj
import writer

class panos_nat_rule:
    playbook_name = ''
    hosts=[]
    register=[]
    destination_zone = ''
    ip_address = ''
    operation = ''
    password = ''
    rule_name = ''
    source_zone = ''
    api_key = ''
    commit = ''
    description = ''
    destination_ip = ''
    devicegroup = ''
    dnat_address = ''
    dnat_port = ''
    service = ''
    snat_address_type = ''
    snat_bidirectional = ''
    snat_dynamic_address = ''
    snat_interface = ''
    snat_interface_address = ''
    snat_static_address = ''
    snat_type = ''
    source_ip = ''
    tag_name = ''
    to_interface = ''
    username = ''
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

