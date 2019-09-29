import random
import string
import os
from register import registerObj
import writer

class vca_vapp:
    playbook_name = ''
    hosts=[]
    register=[]
    vapp_name = ''
    api_version = ''
    gateway_name = ''
    host = ''
    instance_id = ''
    network_mode = ''
    network_name = ''
    operation = ''
    org = ''
    password = ''
    service_type = ''
    state = ''
    template_name = ''
    username = ''
    validate_certs = ''
    vdc_name = ''
    vm_cpus = ''
    vm_memory = ''
    vm_name = ''
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

