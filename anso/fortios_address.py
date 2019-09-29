import random
import string
import os
from register import registerObj
import writer

class fortios_address:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    state = ''
    backup = ''
    backup_filename = ''
    backup_path = ''
    comment = ''
    config_file = ''
    country = ''
    end_ip = ''
    file_mode = ''
    host = ''
    interface = ''
    password = ''
    start_ip = ''
    timeout = ''
    type = ''
    username = ''
    value = ''
    vdom = ''
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

