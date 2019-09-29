import random
import string
import os
from register import registerObj
import writer

class grafana_datasource:
    playbook_name = ''
    hosts=[]
    register=[]
    ds_type = ''
    grafana_url = ''
    name = ''
    url = ''
    access = ''
    aws_access_key = ''
    aws_assume_role_arn = ''
    aws_auth_type = ''
    aws_credentials_profile = ''
    aws_custom_metrics_namespaces = ''
    aws_default_region = ''
    aws_secret_key = ''
    basic_auth_password = ''
    basic_auth_user = ''
    client_cert = ''
    client_key = ''
    database = ''
    es_version = ''
    grafana_api_key = ''
    interval = ''
    is_default = ''
    max_concurrent_shard_requests = ''
    org_id = ''
    password = ''
    sslmode = ''
    state = ''
    time_field = ''
    time_interval = ''
    tls_ca_cert = ''
    tls_client_cert = ''
    tls_client_key = ''
    tls_skip_verify = ''
    trends = ''
    tsdb_resolution = ''
    tsdb_version = ''
    url_password = ''
    url_username = ''
    use_proxy = ''
    user = ''
    validate_certs = ''
    with_credentials = ''
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

