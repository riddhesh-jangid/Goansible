import random
import string
import os
from register import registerObj
import writer

class one_vm:
    playbook_name = ''
    hosts=[]
    register=[]
    api_password = ''
    api_url = ''
    api_username = ''
    attributes = ''
    count = ''
    count_attributes = ''
    count_labels = ''
    cpu = ''
    disk_saveas = ''
    disk_size = ''
    exact_count = ''
    group_id = ''
    hard = ''
    instance_ids = ''
    labels = ''
    memory = ''
    mode = ''
    networks = ''
    owner_id = ''
    state = ''
    template_id = ''
    template_name = ''
    vcpu = ''
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

