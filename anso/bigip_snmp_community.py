import random
import string
import os
from register import registerObj
import writer

class bigip_snmp_community:
    playbook_name = ''
    hosts=[]
    register=[]
    password = ''
    server = ''
    user = ''
    access = ''
    community = ''
    ip_version = ''
    name = ''
    oid = ''
    partition = ''
    port = ''
    provider = ''
    server_port = ''
    snmp_auth_password = ''
    snmp_auth_protocol = ''
    snmp_privacy_password = ''
    snmp_privacy_protocol = ''
    snmp_username = ''
    source = ''
    state = ''
    update_password = ''
    validate_certs = ''
    version = ''
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

