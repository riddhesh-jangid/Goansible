import random
import string
import os
from register import registerObj
import writer

class bigip_qkview:
    playbook_name = ''
    hosts=[]
    register=[]
    dest = ''
    password = ''
    server = ''
    user = ''
    asm_request_log = ''
    complete_information = ''
    exclude = ''
    exclude_core = ''
    filename = ''
    force = ''
    max_file_size = ''
    provider = ''
    server_port = ''
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

