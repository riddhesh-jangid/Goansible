import random
import string
import os
from register import registerObj
import writer

class avi_serverautoscalepolicy:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    api_context = ''
    api_version = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    controller = ''
    description = ''
    intelligent_autoscale = ''
    intelligent_scalein_margin = ''
    intelligent_scaleout_margin = ''
    max_scalein_adjustment_step = ''
    max_scaleout_adjustment_step = ''
    max_size = ''
    min_size = ''
    password = ''
    scalein_alertconfig_refs = ''
    scalein_cooldown = ''
    scaleout_alertconfig_refs = ''
    scaleout_cooldown = ''
    state = ''
    tenant = ''
    tenant_ref = ''
    tenant_uuid = ''
    url = ''
    use_predicted_load = ''
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

