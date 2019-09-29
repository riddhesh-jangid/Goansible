import random
import string
import os
from register import registerObj
import writer

class aci_aaa_user:
    playbook_name = ''
    hosts=[]
    register=[]
    host = ''
    password = ''
    private_key = ''
    aaa_password = ''
    aaa_password_lifetime = ''
    aaa_password_update_required = ''
    aaa_user = ''
    certificate_name = ''
    clear_password_history = ''
    description = ''
    email = ''
    enabled = ''
    expiration = ''
    expires = ''
    first_name = ''
    last_name = ''
    output_level = ''
    phone = ''
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

