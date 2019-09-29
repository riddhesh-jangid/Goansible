import random
import string
import os
from register import registerObj
import writer

class bigip_device_auth_ldap:
    playbook_name = ''
    hosts=[]
    register=[]
    password = ''
    server = ''
    user = ''
    bind_dn = ''
    bind_password = ''
    ca_cert = ''
    check_member_attr = ''
    client_cert = ''
    client_key = ''
    fallback_to_local = ''
    login_ldap_attr = ''
    port = ''
    provider = ''
    remote_directory_tree = ''
    scope = ''
    server_port = ''
    servers = ''
    ssl = ''
    state = ''
    update_password = ''
    user_template = ''
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

