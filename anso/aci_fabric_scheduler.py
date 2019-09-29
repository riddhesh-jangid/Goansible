import random
import string
import os
from register import registerObj
import writer

class aci_fabric_scheduler:
    playbook_name = ''
    hosts=[]
    register=[]
    host = ''
    name = ''
    password = ''
    private_key = ''
    certificate_name = ''
    concurCap = ''
    date = ''
    day = ''
    description = ''
    hour = ''
    maxTime = ''
    minute = ''
    output_level = ''
    port = ''
    recurring = ''
    state = ''
    timeout = ''
    use_proxy = ''
    use_ssl = ''
    username = ''
    validate_certs = ''
    windowname = ''
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

