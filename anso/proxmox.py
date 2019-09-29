import random
import string
import os
from register import registerObj
import writer

class proxmox:
    playbook_name = ''
    hosts=[]
    register=[]
    api_host = ''
    api_user = ''
    api_password = ''
    cores = ''
    cpus = ''
    cpuunits = ''
    disk = ''
    force = ''
    hostname = ''
    ip_address = ''
    memory = ''
    mounts = ''
    nameserver = ''
    netif = ''
    node = ''
    onboot = ''
    ostemplate = ''
    password = ''
    pool = ''
    pubkey = ''
    searchdomain = ''
    state = ''
    storage = ''
    swap = ''
    timeout = ''
    unprivileged = ''
    validate_certs = ''
    vmid = ''
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

