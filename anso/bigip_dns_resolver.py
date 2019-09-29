import random
import string
import os
from register import registerObj
import writer

class bigip_dns_resolver:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    answer_default_zones = ''
    cache_size = ''
    partition = ''
    provider = ''
    randomize_query_case = ''
    route_domain = ''
    server_port = ''
    state = ''
    use_ipv4 = ''
    use_ipv6 = ''
    use_tcp = ''
    use_udp = ''
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

