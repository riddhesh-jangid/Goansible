import random
import string
import os
from register import registerObj
import writer

class panos_object:
    playbook_name = ''
    hosts=[]
    register=[]
    ip_address = ''
    operation = ''
    password = ''
    address = ''
    address_type = ''
    addressgroup = ''
    addressobject = ''
    api_key = ''
    color = ''
    description = ''
    destination_port = ''
    devicegroup = ''
    dynamic_value = ''
    protocol = ''
    servicegroup = ''
    serviceobject = ''
    services = ''
    source_port = ''
    static_value = ''
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

