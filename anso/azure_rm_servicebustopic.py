import random
import string
import os
from register import registerObj
import writer

class azure_rm_servicebustopic:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    namespace = ''
    resource_group = ''
    ad_user = ''
    adfs_authority_url = ''
    api_profile = ''
    append_tags = ''
    auth_source = ''
    auto_delete_on_idle_in_seconds = ''
    cert_validation_mode = ''
    client_id = ''
    cloud_environment = ''
    default_message_time_to_live_seconds = ''
    duplicate_detection_time_in_seconds = ''
    enable_batched_operations = ''
    enable_express = ''
    enable_partitioning = ''
    max_size_in_mb = ''
    password = ''
    profile = ''
    requires_duplicate_detection = ''
    secret = ''
    state = ''
    status = ''
    subscription_id = ''
    support_ordering = ''
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

