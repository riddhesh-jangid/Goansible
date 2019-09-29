import random
import string
import os
from register import registerObj
import writer

class bigip_data_group:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    delete_data_group_file = ''
    description = ''
    external_file_name = ''
    internal = ''
    partition = ''
    provider = ''
    records = ''
    records_src = ''
    separator = ''
    server_port = ''
    state = ''
    type = ''
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

