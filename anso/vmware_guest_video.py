import random
import string
import os
from register import registerObj
import writer

class vmware_guest_video:
    playbook_name = ''
    hosts=[]
    register=[]
    datacenter = ''
    display_number = ''
    enable_3D = ''
    folder = ''
    gather_video_facts = ''
    hostname = ''
    memory_3D_mb = ''
    name = ''
    password = ''
    port = ''
    renderer_3D = ''
    use_auto_detect = ''
    username = ''
    uuid = ''
    validate_certs = ''
    video_memory_mb = ''
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

