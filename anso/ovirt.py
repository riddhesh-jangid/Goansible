import random
import string
import os
from register import registerObj
import writer

class ovirt:
    playbook_name = ''
    hosts=[]
    register=[]
    instance_name = ''
    password = ''
    url = ''
    user = ''
    disk_alloc = ''
    disk_int = ''
    image = ''
    instance_cores = ''
    instance_cpus = ''
    instance_disksize = ''
    instance_dns = ''
    instance_domain = ''
    instance_hostname = ''
    instance_ip = ''
    instance_key = ''
    instance_mem = ''
    instance_netmask = ''
    instance_network = ''
    instance_nic = ''
    instance_os = ''
    instance_rootpw = ''
    instance_type = ''
    region = ''
    resource_type = ''
    sdomain = ''
    state = ''
    zone = ''
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

