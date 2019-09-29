import random
import string
import os
from register import registerObj
import writer

class azure_rm_appgateway:
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
    authentication_certificates = ''
    backend_address_pools = ''
    backend_http_settings_collection = ''
    cert_validation_mode = ''
    client_id = ''
    cloud_environment = ''
    frontend_ip_configurations = ''
    frontend_ports = ''
    gateway_ip_configurations = ''
    http_listeners = ''
    location = ''
    password = ''
    probes = ''
    profile = ''
    redirect_configurations = ''
    request_routing_rules = ''
    secret = ''
    sku = ''
    ssl_certificates = ''
    ssl_policy = ''
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

