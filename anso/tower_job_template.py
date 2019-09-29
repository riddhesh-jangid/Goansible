import random
import string
import os
from register import registerObj
import writer

class tower_job_template:
    playbook_name = ''
    hosts=[]
    register=[]
    job_type = ''
    name = ''
    playbook = ''
    project = ''
    ask_credential = ''
    ask_diff_mode = ''
    ask_extra_vars = ''
    ask_inventory = ''
    ask_job_type = ''
    ask_limit = ''
    ask_skip_tags = ''
    ask_tags = ''
    ask_verbosity = ''
    become_enabled = ''
    concurrent_jobs_enabled = ''
    credential = ''
    description = ''
    diff_mode_enabled = ''
    extra_vars_path = ''
    fact_caching_enabled = ''
    force_handlers_enabled = ''
    forks = ''
    host_config_key = ''
    inventory = ''
    job_tags = ''
    limit = ''
    skip_tags = ''
    start_at_task = ''
    state = ''
    survey_enabled = ''
    survey_spec = ''
    tower_config_file = ''
    tower_host = ''
    tower_password = ''
    tower_username = ''
    validate_certs = ''
    vault_credential = ''
    verbosity = ''
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

