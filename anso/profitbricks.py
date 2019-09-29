import random
import string
import os
from register import registerObj
import writer

class profitbricks:
    playbook_name = ''
    hosts=[]
    register=[]
    image = ''
    name = ''
    assign_public_ip = ''
    auto_increment = ''
    bus = ''
    cores = ''
    count = ''
    cpu_family = ''
    datacenter = ''
    image_password = ''
    instance_ids = ''
    lan = ''
    location = ''
    ram = ''
    remove_boot_volume = ''
    ssh_keys = ''
    state = ''
    subscription_password = ''
    subscription_user = ''
    volume_size = ''
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

