import random
import string
import os
from register import registerObj
import writer

class bigip_firewall_rule:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    action = ''
    description = ''
    destination = ''
    icmp_message = ''
    irule = ''
    logging = ''
    parent_policy = ''
    parent_rule_list = ''
    partition = ''
    protocol = ''
    provider = ''
    rule_list = ''
    schedule = ''
    server_port = ''
    source = ''
    state = ''
    status = ''
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

