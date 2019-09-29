import random
import string
import os
from register import registerObj
import writer

class ce_snmp_target_host:
    playbook_name = ''
    hosts=[]
    register=[]
    address = ''
    connect_port = ''
    host_name = ''
    interface_name = ''
    is_public_net = ''
    notify_type = ''
    recv_port = ''
    security_level = ''
    security_model = ''
    security_name = ''
    security_name_v3 = ''
    version = ''
    vpn_name = ''
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

