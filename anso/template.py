import random
import string
import os
from register import registerObj
import writer

class template:
    playbook_name = ''
    hosts=[]
    register=[]
    dest = ''
    src = ''
    attributes = ''
    backup = ''
    block_end_string = ''
    block_start_string = ''
    follow = ''
    force = ''
    group = ''
    lstrip_blocks = ''
    mode = ''
    newline_sequence = ''
    output_encoding = ''
    owner = ''
    selevel = ''
    serole = ''
    setype = ''
    seuser = ''
    trim_blocks = ''
    unsafe_writes = ''
    validate = ''
    variable_end_string = ''
    variable_start_string = ''
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

