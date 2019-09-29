import random
import string
import os
from register import registerObj
import writer

class bigip_imish_config:
    playbook_name = ''
    hosts=[]
    register=[]
    password = ''
    server = ''
    user = ''
    after = ''
    backup = ''
    backup_options = ''
    before = ''
    diff_against = ''
    diff_ignore_lines = ''
    intended_config = ''
    lines = ''
    match = ''
    parents = ''
    provider = ''
    replace = ''
    route_domain = ''
    running_config = ''
    save_when = ''
    server_port = ''
    src = ''
    validate_certs = ''
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

