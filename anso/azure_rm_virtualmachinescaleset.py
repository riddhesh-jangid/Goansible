import random
import string
import os
from register import registerObj
import writer

class azure_rm_virtualmachinescaleset:
    playbook_name = ''
    hosts=[]
    register=[]
    image = ''
    name = ''
    resource_group = ''
    ad_user = ''
    adfs_authority_url = ''
    admin_password = ''
    admin_username = ''
    api_profile = ''
    append_tags = ''
    application_gateway = ''
    auth_source = ''
    capacity = ''
    cert_validation_mode = ''
    client_id = ''
    cloud_environment = ''
    custom_data = ''
    data_disks = ''
    enable_accelerated_networking = ''
    load_balancer = ''
    location = ''
    managed_disk_type = ''
    os_disk_caching = ''
    os_type = ''
    overprovision = ''
    password = ''
    profile = ''
    remove_on_absent = ''
    secret = ''
    security_group = ''
    short_hostname = ''
    ssh_password_enabled = ''
    ssh_public_keys = ''
    state = ''
    subnet_name = ''
    subscription_id = ''
    tags = ''
    tenant = ''
    tier = ''
    upgrade_policy = ''
    virtual_network_name = ''
    virtual_network_resource_group = ''
    vm_size = ''
    zones = ''
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

