import random
import string
import os
from register import registerObj
import writer

class na_elementsw_snapshot_schedule:
    playbook_name = ''
    hosts=[]
    register=[]
    hostname = ''
    password = ''
    state = ''
    username = ''
    account_id = ''
    days_of_month_hours = ''
    days_of_month_minutes = ''
    days_of_month_monthdays = ''
    days_of_week_hours = ''
    days_of_week_minutes = ''
    days_of_week_weekdays = ''
    name = ''
    paused = ''
    recurring = ''
    retention = ''
    schedule_type = ''
    snapshot_name = ''
    starting_date = ''
    time_interval_days = ''
    time_interval_hours = ''
    time_interval_minutes = ''
    volumes = ''
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

