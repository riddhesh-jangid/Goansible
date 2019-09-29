import random
import string
import os
from register import registerObj
import writer

class fmgr_fwobj_address:
    playbook_name = ''
    hosts=[]
    register=[]
    adom = ''
    allow_routing = ''
    associated_interface = ''
    cache_ttl = ''
    color = ''
    comment = ''
    country = ''
    end_ip = ''
    fqdn = ''
    group_members = ''
    group_name = ''
    ipv4 = ''
    ipv4addr = ''
    ipv6 = ''
    ipv6addr = ''
    mode = ''
    multicast = ''
    name = ''
    obj_id = ''
    start_ip = ''
    visibility = ''
    wildcard = ''
    wildcard_fqdn = ''
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

