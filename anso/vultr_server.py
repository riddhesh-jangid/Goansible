import random
import string
import os
from register import registerObj
import writer

class vultr_server:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    api_account = ''
    api_endpoint = ''
    api_key = ''
    api_retries = ''
    api_timeout = ''
    auto_backup_enabled = ''
    firewall_group = ''
    force = ''
    hostname = ''
    ipv6_enabled = ''
    notify_activate = ''
    os = ''
    plan = ''
    private_network_enabled = ''
    region = ''
    reserved_ip_v4 = ''
    snapshot = ''
    ssh_keys = ''
    startup_script = ''
    state = ''
    tag = ''
    user_data = ''
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

