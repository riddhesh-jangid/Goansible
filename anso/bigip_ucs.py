import random
import string
import os
from register import registerObj
import writer

class bigip_ucs:
    playbook_name = ''
    hosts=[]
    register=[]
    password = ''
    server = ''
    user = ''
    force = ''
    include_chassis_level_config = ''
    no_license = ''
    no_platform_check = ''
    passphrase = ''
    provider = ''
    reset_trust = ''
    server_port = ''
    state = ''
    ucs = ''
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

