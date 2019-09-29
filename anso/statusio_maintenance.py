import random
import string
import os
from register import registerObj
import writer

class statusio_maintenance:
    playbook_name = ''
    hosts=[]
    register=[]
    api_id = ''
    api_key = ''
    statuspage = ''
    all_infrastructure_affected = ''
    automation = ''
    components = ''
    containers = ''
    desc = ''
    maintenance_id = ''
    maintenance_notify_1_hr = ''
    maintenance_notify_24_hr = ''
    maintenance_notify_72_hr = ''
    maintenance_notify_now = ''
    minutes = ''
    start_date = ''
    start_time = ''
    state = ''
    title = ''
    url = ''
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

