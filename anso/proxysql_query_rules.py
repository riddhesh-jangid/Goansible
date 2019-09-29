import random
import string
import os
from register import registerObj
import writer

class proxysql_query_rules:
    playbook_name = ''
    hosts=[]
    register=[]
    active = ''
    apply = ''
    cache_ttl = ''
    client_addr = ''
    comment = ''
    config_file = ''
    delay = ''
    destination_hostgroup = ''
    digest = ''
    error_msg = ''
    flagIN = ''
    flagOUT = ''
    force_delete = ''
    load_to_runtime = ''
    log = ''
    login_host = ''
    login_password = ''
    login_port = ''
    login_user = ''
    match_digest = ''
    match_pattern = ''
    mirror_flagOUT = ''
    mirror_hostgroup = ''
    negate_match_pattern = ''
    proxy_addr = ''
    proxy_port = ''
    replace_pattern = ''
    retries = ''
    rule_id = ''
    save_to_disk = ''
    schemaname = ''
    state = ''
    timeout = ''
    username = ''
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

