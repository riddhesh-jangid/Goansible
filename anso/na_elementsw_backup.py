import random
import string
import os
from register import registerObj
import writer

class na_elementsw_backup:
    playbook_name = ''
    hosts=[]
    register=[]
    dest_volume_id = ''
    hostname = ''
    password = ''
    src_hostname = ''
    src_password = ''
    src_username = ''
    src_volume_id = ''
    username = ''
    dest_hostname = ''
    dest_password = ''
    dest_username = ''
    format = ''
    script = ''
    script_parameters = ''
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

