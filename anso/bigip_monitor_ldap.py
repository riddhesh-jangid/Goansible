import random
import string
import os
from register import registerObj
import writer

class bigip_monitor_ldap:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    base = ''
    chase_referrals = ''
    debug = ''
    description = ''
    filter = ''
    interval = ''
    ip = ''
    mandatory_attributes = ''
    manual_resume = ''
    parent = ''
    partition = ''
    port = ''
    provider = ''
    security = ''
    server_port = ''
    state = ''
    target_password = ''
    target_username = ''
    time_until_up = ''
    timeout = ''
    up_interval = ''
    update_password = ''
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

