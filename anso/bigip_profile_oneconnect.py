import random
import string
import os
from register import registerObj
import writer

class bigip_profile_oneconnect:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    description = ''
    idle_timeout_override = ''
    limit_type = ''
    maximum_age = ''
    maximum_reuse = ''
    maximum_size = ''
    parent = ''
    partition = ''
    provider = ''
    server_port = ''
    share_pools = ''
    source_mask = ''
    state = ''
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

