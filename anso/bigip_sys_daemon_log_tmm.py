import random
import string
import os
from register import registerObj
import writer

class bigip_sys_daemon_log_tmm:
    playbook_name = ''
    hosts=[]
    register=[]
    password = ''
    server = ''
    user = ''
    arp_log_level = ''
    http_compression_log_level = ''
    http_log_level = ''
    ip_log_level = ''
    irule_log_level = ''
    layer4_log_level = ''
    net_log_level = ''
    os_log_level = ''
    provider = ''
    pva_log_level = ''
    server_port = ''
    ssl_log_level = ''
    state = ''
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

