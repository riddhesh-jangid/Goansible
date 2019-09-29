import random
import string
import os
from register import registerObj
import writer

class bigip_gtm_topology_record:
    playbook_name = ''
    hosts=[]
    register=[]
    destination = ''
    password = ''
    server = ''
    source = ''
    user = ''
    partition = ''
    provider = ''
    server_port = ''
    state = ''
    validate_certs = ''
    weight = ''
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

