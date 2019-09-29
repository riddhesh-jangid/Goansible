import random
import string
import os
from register import registerObj
import writer

class aci_bd_to_l3out:
    playbook_name = ''
    hosts=[]
    register=[]
    host = ''
    password = ''
    private_key = ''
    bd = ''
    certificate_name = ''
    l3out = ''
    output_level = ''
    port = ''
    state = ''
    tenant = ''
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

