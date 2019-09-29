import random
import string
import os
from register import registerObj
import writer

class ali_instance:
    playbook_name = ''
    hosts=[]
    register=[]
    alicloud_access_key = ''
    alicloud_region = ''
    alicloud_secret_key = ''
    alicloud_security_token = ''
    allocate_public_ip = ''
    auto_renew = ''
    auto_renew_period = ''
    availability_zone = ''
    count = ''
    count_tag = ''
    description = ''
    force = ''
    host_name = ''
    image_id = ''
    instance_charge_type = ''
    instance_ids = ''
    instance_name = ''
    instance_tags = ''
    instance_type = ''
    internet_charge_type = ''
    key_name = ''
    max_bandwidth_in = ''
    max_bandwidth_out = ''
    password = ''
    period = ''
    security_groups = ''
    state = ''
    system_disk_category = ''
    system_disk_description = ''
    system_disk_name = ''
    system_disk_size = ''
    user_data = ''
    vswitch_id = ''
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

