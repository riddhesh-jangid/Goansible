import random
import string
import os
from register import registerObj
import writer

class postgresql_pg_hba:
    playbook_name = ''
    hosts=[]
    register=[]
    dest = ''
    address = ''
    attributes = ''
    backup = ''
    backup_file = ''
    contype = ''
    create = ''
    databases = ''
    group = ''
    method = ''
    mode = ''
    netmask = ''
    options = ''
    order = ''
    owner = ''
    selevel = ''
    serole = ''
    setype = ''
    seuser = ''
    state = ''
    unsafe_writes = ''
    users = ''
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

