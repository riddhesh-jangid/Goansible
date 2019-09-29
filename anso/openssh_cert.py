import random
import string
import os
from register import registerObj
import writer

class openssh_cert:
    playbook_name = ''
    hosts=[]
    register=[]
    path = ''
    public_key = ''
    signing_key = ''
    type = ''
    valid_from = ''
    valid_to = ''
    attributes = ''
    force = ''
    group = ''
    identifier = ''
    mode = ''
    options = ''
    owner = ''
    principals = ''
    selevel = ''
    serial_number = ''
    serole = ''
    setype = ''
    seuser = ''
    state = ''
    unsafe_writes = ''
    valid_at = ''
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

