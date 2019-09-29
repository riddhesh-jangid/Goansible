import random
import string
import os
from register import registerObj
import writer

class ovirt_event:
    playbook_name = ''
    hosts=[]
    register=[]
    auth = ''
    cluster = ''
    custom_id = ''
    data_center = ''
    description = ''
    fetch_nested = ''
    host = ''
    id = ''
    nested_attributes = ''
    origin = ''
    poll_interval = ''
    severity = ''
    state = ''
    storage_domain = ''
    template = ''
    timeout = ''
    user = ''
    vm = ''
    wait = ''
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

