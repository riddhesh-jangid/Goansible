import random
import string
import os
from register import registerObj
import writer

class proxysql_replication_hostgroups:
    playbook_name = ''
    hosts=[]
    register=[]
    reader_hostgroup = ''
    writer_hostgroup = ''
    comment = ''
    config_file = ''
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

