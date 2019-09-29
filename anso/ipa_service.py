import random
import string
import os
from register import registerObj
import writer

class ipa_service:
    playbook_name = ''
    hosts=[]
    register=[]
    ipa_pass = ''
    krbcanonicalname = ''
    force = ''
    hosts = ''
    ipa_host = ''
    ipa_port = ''
    ipa_prot = ''
    ipa_timeout = ''
    ipa_user = ''
    state = ''
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

