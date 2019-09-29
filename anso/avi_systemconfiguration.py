import random
import string
import os
from register import registerObj
import writer

class avi_systemconfiguration:
    playbook_name = ''
    hosts=[]
    register=[]
    admin_auth_configuration = ''
    api_context = ''
    api_version = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    controller = ''
    default_license_tier = ''
    dns_configuration = ''
    dns_virtualservice_refs = ''
    docker_mode = ''
    email_configuration = ''
    global_tenant_config = ''
    linux_configuration = ''
    mgmt_ip_access_control = ''
    ntp_configuration = ''
    password = ''
    portal_configuration = ''
    proxy_configuration = ''
    snmp_configuration = ''
    ssh_ciphers = ''
    ssh_hmacs = ''
    state = ''
    tenant = ''
    tenant_uuid = ''
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

