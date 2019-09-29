import random
import string
import os
from register import registerObj
import writer

class azure_rm_sqldatabase:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    resource_group = ''
    server_name = ''
    ad_user = ''
    adfs_authority_url = ''
    api_profile = ''
    append_tags = ''
    auth_source = ''
    cert_validation_mode = ''
    client_id = ''
    cloud_environment = ''
    collation = ''
    create_mode = ''
    edition = ''
    elastic_pool_name = ''
    force_update = ''
    location = ''
    max_size_bytes = ''
    password = ''
    profile = ''
    read_scale = ''
    recovery_services_recovery_point_resource_id = ''
    restore_point_in_time = ''
    sample_name = ''
    secret = ''
    source_database_deletion_date = ''
    source_database_id = ''
    state = ''
    subscription_id = ''
    tags = ''
    tenant = ''
    zone_redundant = ''
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

