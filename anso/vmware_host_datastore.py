import random
import string
import os
from register import registerObj
import writer

class vmware_host_datastore:
    playbook_name = ''
    hosts=[]
    register=[]
    datastore_name = ''
    datastore_type = ''
    esxi_hostname = ''
    datacenter_name = ''
    hostname = ''
    nfs_path = ''
    nfs_ro = ''
    nfs_server = ''
    password = ''
    port = ''
    state = ''
    username = ''
    validate_certs = ''
    vmfs_device_name = ''
    vmfs_version = ''
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

