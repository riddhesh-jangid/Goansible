import random
import string
import os
from register import registerObj
import writer

class azure_rm_servicebustopicsubscription:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    namespace = ''
    resource_group = ''
    topic = ''
    ad_user = ''
    adfs_authority_url = ''
    api_profile = ''
    append_tags = ''
    auth_source = ''
    auto_delete_on_idle_in_seconds = ''
    cert_validation_mode = ''
    client_id = ''
    cloud_environment = ''
    dead_lettering_on_filter_evaluation_exceptions = ''
    dead_lettering_on_message_expiration = ''
    default_message_time_to_live_seconds = ''
    duplicate_detection_time_in_seconds = ''
    enable_batched_operations = ''
    forward_dead_lettered_messages_to = ''
    forward_to = ''
    lock_duration_in_seconds = ''
    max_delivery_count = ''
    password = ''
    profile = ''
    requires_session = ''
    secret = ''
    state = ''
    status = ''
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

