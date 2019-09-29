import random
import string
import os
from register import registerObj
import writer

class profitbricks_volume:
    playbook_name = ''
    hosts=[]
    register=[]
    datacenter = ''
    image = ''
    name = ''
    auto_increment = ''
    bus = ''
    count = ''
    disk_type = ''
    image_password = ''
    instance_ids = ''
    licence_type = ''
    size = ''
    ssh_keys = ''
    state = ''
    subscription_password = ''
    subscription_user = ''
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

