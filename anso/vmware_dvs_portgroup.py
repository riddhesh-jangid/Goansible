import random
import string
import os
from register import registerObj
import writer

class vmware_dvs_portgroup:
    playbook_name = ''
    hosts=[]
    register=[]
    num_ports = ''
    portgroup_name = ''
    portgroup_type = ''
    state = ''
    switch_name = ''
    vlan_id = ''
    hostname = ''
    network_policy = ''
    password = ''
    port = ''
    port_policy = ''
    teaming_policy = ''
    username = ''
    validate_certs = ''
    vlan_trunk = ''
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

