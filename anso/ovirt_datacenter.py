import random
import string
import os
from register import registerObj
import writer

class ovirt_datacenter:
    playbook_name = ''
    hosts=[]
    register=[]
    auth = ''
    name = ''
    comment = ''
    compatibility_version = ''
    description = ''
    fetch_nested = ''
    force = ''
    id = ''
    local = ''
    mac_pool = ''
    nested_attributes = ''
    poll_interval = ''
    quota_mode = ''
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

