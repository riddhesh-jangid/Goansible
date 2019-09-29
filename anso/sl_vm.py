import random
import string
import os
from register import registerObj
import writer

class sl_vm:
    playbook_name = ''
    hosts=[]
    register=[]
    cpus = ''
    disks = ''
    memory = ''
    datacenter = ''
    dedicated = ''
    domain = ''
    hostname = ''
    hourly = ''
    image_id = ''
    instance_id = ''
    local_disk = ''
    nic_speed = ''
    os_code = ''
    post_uri = ''
    private = ''
    private_vlan = ''
    public_vlan = ''
    ssh_keys = ''
    state = ''
    tags = ''
    wait = ''
    wait_time = ''
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

