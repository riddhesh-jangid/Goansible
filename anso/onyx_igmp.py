import random
import string
import os
from register import registerObj
import writer

class onyx_igmp:
    playbook_name = ''
    hosts=[]
    register=[]
    state = ''
    default_version = ''
    last_member_query_interval = ''
    mrouter_timeout = ''
    port_purge_timeout = ''
    proxy_reporting = ''
    report_suppression_interval = ''
    unregistered_multicast = ''
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

