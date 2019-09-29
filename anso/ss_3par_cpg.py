import random
import string
import os
from register import registerObj
import writer

class ss_3par_cpg:
    playbook_name = ''
    hosts=[]
    register=[]
    cpg_name = ''
    state = ''
    storage_system_ip = ''
    storage_system_password = ''
    storage_system_username = ''
    disk_type = ''
    domain = ''
    growth_increment = ''
    growth_limit = ''
    growth_warning = ''
    high_availability = ''
    raid_type = ''
    secure = ''
    set_size = ''
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

