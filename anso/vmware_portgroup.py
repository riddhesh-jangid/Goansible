import random
import string
import os
from register import registerObj
import writer

class vmware_portgroup:
    playbook_name = ''
    hosts=[]
    register=[]
    portgroup_name = ''
    switch_name = ''
    vlan_id = ''
    cluster_name = ''
    hostname = ''
    hosts = ''
    network_policy = ''
    password = ''
    port = ''
    state = ''
    teaming_policy = ''
    username = ''
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

