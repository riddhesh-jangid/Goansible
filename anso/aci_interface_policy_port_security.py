import random
import string
import os
from register import registerObj
import writer

class aci_interface_policy_port_security:
    playbook_name = ''
    hosts=[]
    register=[]
    host = ''
    password = ''
    port_security = ''
    private_key = ''
    certificate_name = ''
    description = ''
    max_end_points = ''
    output_level = ''
    port = ''
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

