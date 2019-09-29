import random
import string
import os
from register import registerObj
import writer

class mongodb_replicaset:
    playbook_name = ''
    hosts=[]
    register=[]
    arbiter_at_index = ''
    chaining_allowed = ''
    election_timeout_millis = ''
    heartbeat_timeout_secs = ''
    login_database = ''
    login_host = ''
    login_password = ''
    login_port = ''
    login_user = ''
    members = ''
    protocol_version = ''
    replica_set = ''
    ssl = ''
    ssl_cert_reqs = ''
    validate = ''
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

