import random
import string
import os
from register import registerObj
import writer

class bigiq_device_discovery:
    playbook_name = ''
    hosts=[]
    register=[]
    device_address = ''
    password = ''
    server = ''
    user = ''
    access_conflict_policy = ''
    access_group_first_device = ''
    access_group_name = ''
    conflict_policy = ''
    device_conflict_policy = ''
    device_password = ''
    device_port = ''
    device_username = ''
    force = ''
    ha_name = ''
    modules = ''
    provider = ''
    server_port = ''
    state = ''
    statistics = ''
    use_bigiq_sync = ''
    validate_certs = ''
    versioned_conflict_policy = ''
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

