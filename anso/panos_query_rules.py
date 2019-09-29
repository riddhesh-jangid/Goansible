import random
import string
import os
from register import registerObj
import writer

class panos_query_rules:
    playbook_name = ''
    hosts=[]
    register=[]
    ip_address = ''
    password = ''
    api_key = ''
    application = ''
    destination_ip = ''
    destination_port = ''
    destination_zone = ''
    devicegroup = ''
    protocol = ''
    source_ip = ''
    source_port = ''
    source_zone = ''
    tag_name = ''
    username = ''
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

