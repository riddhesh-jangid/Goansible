import random
import string
import os
from register import registerObj
import writer

class na_ontap_volume:
    playbook_name = ''
    hosts=[]
    register=[]
    hostname = ''
    name = ''
    password = ''
    username = ''
    vserver = ''
    aggr_list = ''
    aggr_list_multiplier = ''
    aggregate_name = ''
    atime_update = ''
    auto_provision_as = ''
    efficiency_policy = ''
    encrypt = ''
    from_name = ''
    http_port = ''
    https = ''
    is_infinite = ''
    is_online = ''
    junction_path = ''
    language = ''
    ontapi = ''
    percent_snapshot_space = ''
    policy = ''
    size = ''
    size_unit = ''
    snapdir_access = ''
    snapshot_policy = ''
    space_guarantee = ''
    state = ''
    time_out = ''
    type = ''
    unix_permissions = ''
    validate_certs = ''
    volume_security_style = ''
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

