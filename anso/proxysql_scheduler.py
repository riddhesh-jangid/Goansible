import random
import string
import os
from register import registerObj
import writer

class proxysql_scheduler:
    playbook_name = ''
    hosts=[]
    register=[]
    filename = ''
    active = ''
    arg1 = ''
    arg2 = ''
    arg3 = ''
    arg4 = ''
    arg5 = ''
    comment = ''
    config_file = ''
    force_delete = ''
    interval_ms = ''
    load_to_runtime = ''
    login_host = ''
    login_password = ''
    login_port = ''
    login_user = ''
    save_to_disk = ''
    state = ''
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

