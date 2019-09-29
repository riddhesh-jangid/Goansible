import random
import string
import os
from register import registerObj
import writer

class aerospike_migrations:
    playbook_name = ''
    hosts=[]
    register=[]
    local_only = ''
    connect_timeout = ''
    consecutive_good_checks = ''
    fail_on_cluster_change = ''
    host = ''
    migrate_rx_key = ''
    migrate_tx_key = ''
    min_cluster_size = ''
    port = ''
    sleep_between_checks = ''
    target_cluster_size = ''
    tries_limit = ''
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

