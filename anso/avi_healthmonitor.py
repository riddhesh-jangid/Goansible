import random
import string
import os
from register import registerObj
import writer

class avi_healthmonitor:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    type = ''
    api_context = ''
    api_version = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    controller = ''
    description = ''
    dns_monitor = ''
    external_monitor = ''
    failed_checks = ''
    http_monitor = ''
    https_monitor = ''
    is_federated = ''
    monitor_port = ''
    password = ''
    receive_timeout = ''
    send_interval = ''
    state = ''
    successful_checks = ''
    tcp_monitor = ''
    tenant = ''
    tenant_ref = ''
    tenant_uuid = ''
    udp_monitor = ''
    url = ''
    username = ''
    uuid = ''
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

