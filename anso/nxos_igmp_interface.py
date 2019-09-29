import random
import string
import os
from register import registerObj
import writer

class nxos_igmp_interface:
    playbook_name = ''
    hosts=[]
    register=[]
    interface = ''
    group_timeout = ''
    immediate_leave = ''
    last_member_qrt = ''
    last_member_query_count = ''
    oif_prefix = ''
    oif_ps = ''
    oif_routemap = ''
    oif_source = ''
    provider = ''
    querier_timeout = ''
    query_interval = ''
    query_mrt = ''
    report_llg = ''
    restart = ''
    robustness = ''
    startup_query_count = ''
    startup_query_interval = ''
    state = ''
    version = ''
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

