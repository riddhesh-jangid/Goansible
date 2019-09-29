import random
import string
import os
from register import registerObj
import writer

class ce_aaa_server_host:
    playbook_name = ''
    hosts=[]
    register=[]
    hwtacacs_is_public_net = ''
    hwtacacs_is_secondary_server = ''
    hwtacacs_server_host_name = ''
    hwtacacs_server_ip = ''
    hwtacacs_server_ipv6 = ''
    hwtacacs_server_type = ''
    hwtacacs_template = ''
    hwtacacs_vpn_name = ''
    local_ftp_dir = ''
    local_password = ''
    local_service_type = ''
    local_user_group = ''
    local_user_level = ''
    local_user_name = ''
    radius_group_name = ''
    radius_server_ip = ''
    radius_server_ipv6 = ''
    radius_server_mode = ''
    radius_server_name = ''
    radius_server_port = ''
    radius_server_type = ''
    radius_vpn_name = ''
    state = ''
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

