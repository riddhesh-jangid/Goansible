import random
import string
import os
from register import registerObj
import writer

class packet_device:
    playbook_name = ''
    hosts=[]
    register=[]
    project_id = ''
    always_pxe = ''
    auth_token = ''
    count = ''
    count_offset = ''
    device_ids = ''
    facility = ''
    features = ''
    hostnames = ''
    ipxe_script_url = ''
    locked = ''
    operating_system = ''
    plan = ''
    state = ''
    user_data = ''
    wait_for_public_IPv = ''
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

