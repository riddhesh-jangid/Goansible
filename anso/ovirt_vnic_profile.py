import random
import string
import os
from register import registerObj
import writer

class ovirt_vnic_profile:
    playbook_name = ''
    hosts=[]
    register=[]
    auth = ''
    data_center = ''
    name = ''
    network = ''
    custom_properties = ''
    description = ''
    fetch_nested = ''
    migratable = ''
    nested_attributes = ''
    network_filter = ''
    pass_through = ''
    poll_interval = ''
    port_mirroring = ''
    qos = ''
    state = ''
    timeout = ''
    wait = ''
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

