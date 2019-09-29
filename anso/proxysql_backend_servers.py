import random
import string
import os
from register import registerObj
import writer

class proxysql_backend_servers:
    playbook_name = ''
    hosts=[]
    register=[]
    hostname = ''
    comment = ''
    compression = ''
    config_file = ''
    hostgroup_id = ''
    load_to_runtime = ''
    login_host = ''
    login_password = ''
    login_port = ''
    login_user = ''
    max_connections = ''
    max_latency_ms = ''
    max_replication_lag = ''
    port = ''
    save_to_disk = ''
    state = ''
    status = ''
    use_ssl = ''
    weight = ''
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

