import random
import string
import os
from register import registerObj
import writer

class ios_vrf:
    playbook_name = ''
    hosts=[]
    register=[]
    associated_interfaces = ''
    auth_pass = ''
    authorize = ''
    delay = ''
    description = ''
    interfaces = ''
    name = ''
    provider = ''
    purge = ''
    rd = ''
    route_both = ''
    route_both_ipv4 = ''
    route_both_ipv6 = ''
    route_export = ''
    route_export_ipv4 = ''
    route_export_ipv6 = ''
    route_import = ''
    route_import_ipv4 = ''
    route_import_ipv6 = ''
    state = ''
    vrfs = ''
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

