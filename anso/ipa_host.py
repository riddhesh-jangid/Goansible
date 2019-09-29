import random
import string
import os
from register import registerObj
import writer

class ipa_host:
    playbook_name = ''
    hosts=[]
    register=[]
    fqdn = ''
    ipa_pass = ''
    description = ''
    force = ''
    ip_address = ''
    ipa_host = ''
    ipa_port = ''
    ipa_prot = ''
    ipa_timeout = ''
    ipa_user = ''
    mac_address = ''
    ns_hardware_platform = ''
    ns_host_location = ''
    ns_os_version = ''
    random_password = ''
    state = ''
    update_dns = ''
    user_certificate = ''
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

