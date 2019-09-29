import random
import string
import os
from register import registerObj
import writer

class vmware_vmkernel:
    playbook_name = ''
    hosts=[]
    register=[]
    esxi_hostname = ''
    portgroup_name = ''
    device = ''
    dvswitch_name = ''
    enable_ft = ''
    enable_mgmt = ''
    enable_provisioning = ''
    enable_replication = ''
    enable_replication_nfc = ''
    enable_vmotion = ''
    enable_vsan = ''
    hostname = ''
    ip_address = ''
    mtu = ''
    network = ''
    password = ''
    port = ''
    state = ''
    subnet_mask = ''
    username = ''
    validate_certs = ''
    vswitch_name = ''
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

