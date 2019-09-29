import random
import string
import os
from register import registerObj
import writer

class mso_schema_template_bd_subnet:
    playbook_name = ''
    hosts=[]
    register=[]
    bd = ''
    host = ''
    password = ''
    schema = ''
    subnet = ''
    template = ''
    description = ''
    no_default_gateway = ''
    output_level = ''
    port = ''
    scope = ''
    shared = ''
    state = ''
    timeout = ''
    use_proxy = ''
    use_ssl = ''
    username = ''
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

