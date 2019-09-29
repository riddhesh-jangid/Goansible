import random
import string
import os
from register import registerObj
import writer

class bigip_device_syslog:
    playbook_name = ''
    hosts=[]
    register=[]
    password = ''
    server = ''
    user = ''
    auth_priv_from = ''
    auth_priv_to = ''
    console_log = ''
    cron_from = ''
    cron_to = ''
    daemon_from = ''
    daemon_to = ''
    include = ''
    iso_date = ''
    kern_from = ''
    kern_to = ''
    local6_from = ''
    local6_to = ''
    mail_from = ''
    mail_to = ''
    messages_from = ''
    messages_to = ''
    provider = ''
    server_port = ''
    user_log_from = ''
    user_log_to = ''
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

