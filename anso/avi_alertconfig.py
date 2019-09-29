import random
import string
import os
from register import registerObj
import writer

class avi_alertconfig:
    playbook_name = ''
    hosts=[]
    register=[]
    alert_rule = ''
    category = ''
    name = ''
    source = ''
    action_group_ref = ''
    api_context = ''
    api_version = ''
    autoscale_alert = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    controller = ''
    description = ''
    enabled = ''
    expiry_time = ''
    obj_uuid = ''
    object_type = ''
    password = ''
    recommendation = ''
    rolling_window = ''
    state = ''
    summary = ''
    tenant = ''
    tenant_ref = ''
    tenant_uuid = ''
    threshold = ''
    throttle = ''
    url = ''
    username = ''
    uuid = ''
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

