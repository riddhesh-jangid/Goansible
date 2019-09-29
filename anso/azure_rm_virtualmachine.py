import random
import string
import os
from register import registerObj
import writer

class azure_rm_virtualmachine:
    playbook_name = ''
    hosts=[]
    register=[]
    image = ''
    name = ''
    resource_group = ''
    accept_terms = ''
    ad_user = ''
    adfs_authority_url = ''
    admin_password = ''
    admin_username = ''
    allocated = ''
    api_profile = ''
    append_tags = ''
    auth_source = ''
    availability_set = ''
    cert_validation_mode = ''
    client_id = ''
    cloud_environment = ''
    custom_data = ''
    data_disks = ''
    generalized = ''
    license_type = ''
    location = ''
    managed_disk_type = ''
    network_interface_names = ''
    open_ports = ''
    os_disk_caching = ''
    os_disk_name = ''
    os_disk_size_gb = ''
    os_type = ''
    password = ''
    plan = ''
    profile = ''
    public_ip_allocation_method = ''
    remove_on_absent = ''
    restarted = ''
    secret = ''
    short_hostname = ''
    ssh_password_enabled = ''
    ssh_public_keys = ''
    started = ''
    state = ''
    storage_account_name = ''
    storage_blob_name = ''
    storage_container_name = ''
    subnet_name = ''
    subscription_id = ''
    tags = ''
    tenant = ''
    virtual_network_name = ''
    virtual_network_resource_group = ''
    vm_identity = ''
    vm_size = ''
    winrm = ''
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

