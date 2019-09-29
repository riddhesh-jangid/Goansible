import random
import string
import os
from register import registerObj
import writer

class zabbix_action:
    playbook_name = ''
    hosts=[]
    register=[]
    event_source = ''
    http_login_user = ''
    login_password = ''
    login_user = ''
    name = ''
    server_url = ''
    acknowledge_default_message = ''
    acknowledge_default_subject = ''
    acknowledge_operations = ''
    conditions = ''
    default_message = ''
    default_subject = ''
    esc_period = ''
    eval_type = ''
    formula = ''
    http_login_password = ''
    operations = ''
    pause_in_maintenance = ''
    recovery_default_message = ''
    recovery_default_subject = ''
    recovery_operations = ''
    state = ''
    status = ''
    timeout = ''
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

