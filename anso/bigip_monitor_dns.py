import random
import string
import os
from register import registerObj
import writer

class bigip_monitor_dns:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    accept_rcode = ''
    adaptive = ''
    adaptive_limit = ''
    allowed_divergence_type = ''
    allowed_divergence_value = ''
    answer_section_contains = ''
    description = ''
    interval = ''
    ip = ''
    manual_resume = ''
    parent = ''
    partition = ''
    port = ''
    provider = ''
    query_name = ''
    query_type = ''
    receive = ''
    reverse = ''
    sampling_timespan = ''
    server_port = ''
    state = ''
    time_until_up = ''
    timeout = ''
    transparent = ''
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

