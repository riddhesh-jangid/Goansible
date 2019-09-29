import random
import string
import os
from register import registerObj
import writer

class datadog_monitor:
    playbook_name = ''
    hosts=[]
    register=[]
    api_key = ''
    app_key = ''
    name = ''
    state = ''
    escalation_message = ''
    evaluation_delay = ''
    id = ''
    locked = ''
    message = ''
    new_host_delay = ''
    no_data_timeframe = ''
    notify_audit = ''
    notify_no_data = ''
    query = ''
    renotify_interval = ''
    require_full_window = ''
    silenced = ''
    tags = ''
    thresholds = ''
    timeout_h = ''
    type = ''
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

