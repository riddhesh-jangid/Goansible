import random
import string
import os
from register import registerObj
import writer

class azure_rm_networkinterface:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    resource_group = ''
    subnet_name = ''
    virtual_network = ''
    ad_user = ''
    adfs_authority_url = ''
    api_profile = ''
    append_tags = ''
    auth_source = ''
    cert_validation_mode = ''
    client_id = ''
    cloud_environment = ''
    create_with_security_group = ''
    dns_servers = ''
    enable_accelerated_networking = ''
    enable_ip_forwarding = ''
    ip_configurations = ''
    location = ''
    open_ports = ''
    os_type = ''
    password = ''
    private_ip_address = ''
    private_ip_allocation_method = ''
    profile = ''
    public_ip = ''
    public_ip_address_name = ''
    public_ip_allocation_method = ''
    secret = ''
    security_group = ''
    state = ''
    subscription_id = ''
    tags = ''
    tenant = ''
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

