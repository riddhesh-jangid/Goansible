import random
import string
import os
from register import registerObj
import writer

class zabbix_host:
    playbook_name = ''
    hosts=[]
    register=[]
    host_name = ''
    http_login_user = ''
    login_password = ''
    login_user = ''
    server_url = ''
    ca_cert = ''
    description = ''
    force = ''
    host_groups = ''
    http_login_password = ''
    interfaces = ''
    inventory_mode = ''
    inventory_zabbix = ''
    ipmi_authtype = ''
    ipmi_password = ''
    ipmi_privilege = ''
    ipmi_username = ''
    link_templates = ''
    proxy = ''
    state = ''
    status = ''
    timeout = ''
    tls_accept = ''
    tls_connect = ''
    tls_psk = ''
    tls_psk_identity = ''
    tls_subject = ''
    validate_certs = ''
    visible_name = ''
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

