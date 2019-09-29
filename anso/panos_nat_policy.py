import random
import string
import os
from register import registerObj
import writer

class panos_nat_policy:
    playbook_name = ''
    hosts=[]
    register=[]
    from_zone = ''
    ip_address = ''
    password = ''
    rule_name = ''
    to_zone = ''
    commit = ''
    destination = ''
    dnat_address = ''
    dnat_port = ''
    override = ''
    service = ''
    snat_address = ''
    snat_bidirectional = ''
    snat_interface = ''
    snat_interface_address = ''
    snat_type = ''
    source = ''
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

