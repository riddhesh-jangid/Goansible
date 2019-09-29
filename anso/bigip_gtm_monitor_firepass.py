import random
import string
import os
from register import registerObj
import writer

class bigip_gtm_monitor_firepass:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    cipher_list = ''
    concurrency_limit = ''
    ignore_down_response = ''
    interval = ''
    ip = ''
    max_load_average = ''
    parent = ''
    partition = ''
    port = ''
    probe_timeout = ''
    provider = ''
    server_port = ''
    state = ''
    target_password = ''
    target_username = ''
    timeout = ''
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

