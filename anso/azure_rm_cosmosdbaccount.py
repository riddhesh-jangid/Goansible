import random
import string
import os
from register import registerObj
import writer

class azure_rm_cosmosdbaccount:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    resource_group = ''
    ad_user = ''
    adfs_authority_url = ''
    api_profile = ''
    append_tags = ''
    auth_source = ''
    cert_validation_mode = ''
    client_id = ''
    cloud_environment = ''
    consistency_policy = ''
    database_account_offer_type = ''
    enable_automatic_failover = ''
    enable_cassandra = ''
    enable_gremlin = ''
    enable_multiple_write_locations = ''
    enable_table = ''
    geo_rep_locations = ''
    ip_range_filter = ''
    is_virtual_network_filter_enabled = ''
    kind = ''
    location = ''
    password = ''
    profile = ''
    secret = ''
    state = ''
    subscription_id = ''
    tags = ''
    tenant = ''
    virtual_network_rules = ''
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

