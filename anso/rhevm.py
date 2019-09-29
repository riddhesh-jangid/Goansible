import random
import string
import os
from register import registerObj
import writer

class rhevm:
    playbook_name = ''
    hosts=[]
    register=[]
    boot_order = ''
    cd_drive = ''
    cluster = ''
    cpu_share = ''
    datacenter = ''
    del_prot = ''
    disks = ''
    ifaces = ''
    image = ''
    insecure_api = ''
    mempol = ''
    name = ''
    osver = ''
    password = ''
    port = ''
    server = ''
    state = ''
    timeout = ''
    type = ''
    user = ''
    vm_ha = ''
    vmcpu = ''
    vmhost = ''
    vmmem = ''
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

