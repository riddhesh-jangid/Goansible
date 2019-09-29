import random
import string
import os
from register import registerObj
import writer

class keycloak_client:
    playbook_name = ''
    hosts=[]
    register=[]
    auth_client_id = ''
    auth_keycloak_url = ''
    auth_password = ''
    auth_realm = ''
    auth_username = ''
    admin_url = ''
    attributes = ''
    auth_client_secret = ''
    authorization_services_enabled = ''
    authorization_settings = ''
    base_url = ''
    bearer_only = ''
    client_authenticator_type = ''
    client_id = ''
    client_template = ''
    consent_required = ''
    default_roles = ''
    description = ''
    direct_access_grants_enabled = ''
    enabled = ''
    frontchannel_logout = ''
    full_scope_allowed = ''
    id = ''
    implicit_flow_enabled = ''
    name = ''
    node_re_registration_timeout = ''
    not_before = ''
    protocol = ''
    protocol_mappers = ''
    public_client = ''
    realm = ''
    redirect_uris = ''
    registered_nodes = ''
    registration_access_token = ''
    root_url = ''
    secret = ''
    service_accounts_enabled = ''
    standard_flow_enabled = ''
    state = ''
    surrogate_auth_required = ''
    use_template_config = ''
    use_template_mappers = ''
    use_template_scope = ''
    validate_certs = ''
    web_origins = ''
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

