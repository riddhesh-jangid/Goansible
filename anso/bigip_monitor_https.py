import random
import string
import os
from register import registerObj
import writer

class bigip_monitor_https:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    description = ''
    interval = ''
    ip = ''
    parent = ''
    partition = ''
    port = ''
    provider = ''
    receive = ''
    receive_disable = ''
    send = ''
    server_port = ''
    ssl_profile = ''
    state = ''
    target_password = ''
    target_username = ''
    time_until_up = ''
    timeout = ''
    up_interval = ''
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

