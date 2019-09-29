import random
import string
import os
from register import registerObj
import writer

class pulp_repo:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    relative_url = ''
    add_export_distributor = ''
    ca_cert = ''
    client_cert = ''
    client_key = ''
    feed = ''
    force = ''
    force_basic_auth = ''
    generate_sqlite = ''
    http_agent = ''
    proxy_host = ''
    proxy_password = ''
    proxy_port = ''
    proxy_username = ''
    publish_distributor = ''
    pulp_host = ''
    repo_type = ''
    repoview = ''
    serve_http = ''
    serve_https = ''
    state = ''
    url = ''
    url_password = ''
    url_username = ''
    use_proxy = ''
    validate_certs = ''
    wait_for_completion = ''
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

