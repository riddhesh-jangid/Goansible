import random
import string
import os
from register import registerObj
import writer

class bigip_monitor_snmp_dca:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    agent_type = ''
    community = ''
    cpu_coefficient = ''
    cpu_threshold = ''
    description = ''
    disk_coefficient = ''
    disk_threshold = ''
    interval = ''
    memory_coefficient = ''
    memory_threshold = ''
    parent = ''
    partition = ''
    provider = ''
    server_port = ''
    state = ''
    time_until_up = ''
    timeout = ''
    validate_certs = ''
    version = ''
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

