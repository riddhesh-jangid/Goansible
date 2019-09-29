import random
import string
import os
from register import registerObj
import writer

class na_ontap_autosupport:
    playbook_name = ''
    hosts=[]
    register=[]
    hostname = ''
    node_name = ''
    password = ''
    username = ''
    from_address = ''
    hostname_in_subject = ''
    http_port = ''
    https = ''
    mail_hosts = ''
    noteto = ''
    ontapi = ''
    partner_addresses = ''
    post_url = ''
    proxy_url = ''
    state = ''
    support = ''
    to_addresses = ''
    transport = ''
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

