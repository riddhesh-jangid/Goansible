import random
import string
import os
from register import registerObj
import writer

class ovirt_storage_connection:
    playbook_name = ''
    hosts=[]
    register=[]
    auth = ''
    address = ''
    fetch_nested = ''
    force = ''
    id = ''
    mount_options = ''
    nested_attributes = ''
    nfs_retrans = ''
    nfs_timeout = ''
    nfs_version = ''
    password = ''
    path = ''
    poll_interval = ''
    port = ''
    state = ''
    storage = ''
    target = ''
    timeout = ''
    type = ''
    username = ''
    vfs_type = ''
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

