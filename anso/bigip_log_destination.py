import random
import string
import os
from register import registerObj
import writer

class bigip_log_destination:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    type = ''
    user = ''
    address = ''
    description = ''
    distribution = ''
    forward_to = ''
    partition = ''
    pool = ''
    pool_settings = ''
    port = ''
    protocol = ''
    provider = ''
    server_port = ''
    server_ssl_profile = ''
    state = ''
    syslog_format = ''
    syslog_settings = ''
    template_delete_delay = ''
    template_retransmit_interval = ''
    transport_profile = ''
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

