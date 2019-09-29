import random
import string
import os
from register import registerObj
import writer

class netscaler_server:
    playbook_name = ''
    hosts=[]
    register=[]
    nitro_pass = ''
    nitro_user = ''
    nsip = ''
    comment = ''
    delay = ''
    disabled = ''
    domain = ''
    domainresolveretry = ''
    graceful = ''
    ipaddress = ''
    ipv6address = ''
    name = ''
    nitro_protocol = ''
    nitro_timeout = ''
    save_config = ''
    state = ''
    td = ''
    translationip = ''
    translationmask = ''
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

