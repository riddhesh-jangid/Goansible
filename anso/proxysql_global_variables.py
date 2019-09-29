import random
import string
import os
from register import registerObj
import writer

class proxysql_global_variables:
    playbook_name = ''
    hosts=[]
    register=[]
    variable = ''
    config_file = ''
    load_to_runtime = ''
    login_host = ''
    login_password = ''
    login_port = ''
    login_user = ''
    save_to_disk = ''
    value = ''
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

