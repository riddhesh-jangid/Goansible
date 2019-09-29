import random
import string
import os
from register import registerObj
import writer

class bigip_profile_dns:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    cache_name = ''
    enable_cache = ''
    enable_dns_express = ''
    enable_dns_firewall = ''
    enable_dnssec = ''
    enable_gtm = ''
    enable_zone_transfer = ''
    parent = ''
    partition = ''
    process_recursion_desired = ''
    provider = ''
    server_port = ''
    state = ''
    unhandled_query_action = ''
    use_local_bind = ''
    validate_certs = ''
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

