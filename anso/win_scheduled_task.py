import random
import string
import os
from register import registerObj
import writer

class win_scheduled_task:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    actions = ''
    allow_demand_start = ''
    allow_hard_terminate = ''
    author = ''
    compatibility = ''
    date = ''
    delete_expired_task_after = ''
    description = ''
    disallow_start_if_on_batteries = ''
    display_name = ''
    enabled = ''
    execution_time_limit = ''
    group = ''
    hidden = ''
    logon_type = ''
    multiple_instances = ''
    password = ''
    path = ''
    priority = ''
    restart_count = ''
    restart_interval = ''
    run_level = ''
    run_only_if_idle = ''
    run_only_if_network_available = ''
    source = ''
    start_when_available = ''
    state = ''
    stop_if_going_on_batteries = ''
    triggers = ''
    update_password = ''
    username = ''
    version = ''
    wake_to_run = ''
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

