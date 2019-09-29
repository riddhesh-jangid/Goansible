import random
import string
import os
from register import registerObj
import writer

class vmware_deploy_ovf:
    playbook_name = ''
    hosts=[]
    register=[]
    allow_duplicates = ''
    cluster = ''
    datacenter = ''
    datastore = ''
    deployment_option = ''
    disk_provisioning = ''
    fail_on_spec_warnings = ''
    folder = ''
    hostname = ''
    inject_ovf_env = ''
    name = ''
    networks = ''
    ovf = ''
    password = ''
    port = ''
    power_on = ''
    properties = ''
    resource_pool = ''
    username = ''
    validate_certs = ''
    wait = ''
    wait_for_ip_address = ''
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

