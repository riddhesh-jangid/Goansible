import random
import string
import os
from register import registerObj
import writer

class aci_aaa_user_certificate:
    playbook_name = ''
    hosts=[]
    register=[]
    aaa_user = ''
    host = ''
    password = ''
    private_key = ''
    aaa_user_type = ''
    certificate = ''
    certificate_name = ''
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

