import random
import string
import os
from register import registerObj
import writer

class nios_member:
    playbook_name = ''
    hosts=[]
    register=[]
    host_name = ''
    ipv6_setting = ''
    vip_setting = ''
    comment = ''
    config_addr_type = ''
    create_token = ''
    enable_ha = ''
    extattrs = ''
    external_syslog_server_enable = ''
    lan2_enabled = ''
    lan2_port_setting = ''
    mgmt_port_setting = ''
    node_info = ''
    platform = ''
    pre_provisioning = ''
    provider = ''
    router_id = ''
    state = ''
    syslog_servers = ''
    upgrade_group = ''
    use_syslog_proxy_setting = ''
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

