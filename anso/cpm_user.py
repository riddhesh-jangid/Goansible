import random
import string
import os
from register import registerObj
import writer

class cpm_user:
    playbook_name = ''
    hosts=[]
    register=[]
    cpm_action = ''
    cpm_password = ''
    cpm_url = ''
    cpm_username = ''
    user_name = ''
    use_https = ''
    use_proxy = ''
    user_accessapi = ''
    user_accesslevel = ''
    user_accessmonitor = ''
    user_accessoutbound = ''
    user_accessserial = ''
    user_accessssh = ''
    user_accessweb = ''
    user_callbackphone = ''
    user_groupaccess = ''
    user_pass = ''
    user_plugaccess = ''
    user_portaccess = ''
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

