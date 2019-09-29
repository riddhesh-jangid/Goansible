import random
import string
import os
from register import registerObj
import writer

class digital_ocean:
    playbook_name = ''
    hosts=[]
    register=[]
    api_token = ''
    backups_enabled = ''
    command = ''
    id = ''
    image_id = ''
    ipv6 = ''
    name = ''
    private_networking = ''
    region_id = ''
    size_id = ''
    ssh_key_ids = ''
    ssh_pub_key = ''
    state = ''
    unique_name = ''
    user_data = ''
    virtio = ''
    wait = ''
    wait_timeout = ''
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

