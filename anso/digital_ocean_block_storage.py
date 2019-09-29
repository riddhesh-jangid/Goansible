import random
import string
import os
from register import registerObj
import writer

class digital_ocean_block_storage:
    playbook_name = ''
    hosts=[]
    register=[]
    command = ''
    region = ''
    state = ''
    volume_name = ''
    block_size = ''
    description = ''
    droplet_id = ''
    oauth_token = ''
    snapshot_id = ''
    timeout = ''
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

