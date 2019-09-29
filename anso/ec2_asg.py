import random
import string
import os
from register import registerObj
import writer

class ec2_asg:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    availability_zones = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    default_cooldown = ''
    desired_capacity = ''
    ec2_url = ''
    health_check_period = ''
    health_check_type = ''
    launch_config_name = ''
    launch_template = ''
    lc_check = ''
    load_balancers = ''
    lt_check = ''
    max_size = ''
    metrics_collection = ''
    metrics_granularity = ''
    metrics_list = ''
    min_size = ''
    notification_topic = ''
    notification_types = ''
    placement_group = ''
    profile = ''
    region = ''
    replace_all_instances = ''
    replace_batch_size = ''
    replace_instances = ''
    security_token = ''
    state = ''
    suspend_processes = ''
    tags = ''
    target_group_arns = ''
    termination_policies = ''
    validate_certs = ''
    vpc_zone_identifier = ''
    wait_for_instances = ''
    wait_timeout = ''
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

