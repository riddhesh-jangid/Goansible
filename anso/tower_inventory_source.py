import random
import string
import os
from register import registerObj
import writer

class tower_inventory_source:
    playbook_name = ''
    hosts=[]
    register=[]
    inventory = ''
    name = ''
    source = ''
    credential = ''
    description = ''
    group_by = ''
    instance_filters = ''
    overwrite = ''
    overwrite_vars = ''
    source_path = ''
    source_project = ''
    source_regions = ''
    source_script = ''
    source_vars = ''
    state = ''
    timeout = ''
    tower_config_file = ''
    tower_host = ''
    tower_password = ''
    tower_username = ''
    update_cache_timeout = ''
    update_on_launch = ''
    update_on_project_update = ''
    validate_certs = ''
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

