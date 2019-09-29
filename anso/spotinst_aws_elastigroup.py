import random
import string
import os
from register import registerObj
import writer

class spotinst_aws_elastigroup:
    playbook_name = ''
    hosts=[]
    register=[]
    availability_vs_cost = ''
    availability_zones = ''
    image_id = ''
    key_pair = ''
    max_size = ''
    min_size = ''
    monitoring = ''
    name = ''
    on_demand_instance_type = ''
    product = ''
    security_group_ids = ''
    spot_instance_types = ''
    target = ''
    unit = ''
    account_id = ''
    block_device_mappings = ''
    chef = ''
    credentials_path = ''
    down_scaling_policies = ''
    draining_timeout = ''
    ebs_optimized = ''
    ebs_volume_pool = ''
    ecs = ''
    elastic_ips = ''
    fallback_to_od = ''
    health_check_grace_period = ''
    health_check_type = ''
    health_check_unhealthy_duration_before_replacement = ''
    iam_role_arn = ''
    iam_role_name = ''
    id = ''
    ignore_changes = ''
    kubernetes = ''
    lifetime_period = ''
    load_balancers = ''
    mesosphere = ''
    network_interfaces = ''
    on_demand_count = ''
    opsworks = ''
    persistence = ''
    rancher = ''
    right_scale = ''
    risk = ''
    roll_config = ''
    scheduled_tasks = ''
    shutdown_script = ''
    signals = ''
    spin_up_time = ''
    state = ''
    tags = ''
    target_group_arns = ''
    target_tracking_policies = ''
    tenancy = ''
    terminate_at_end_of_billing_hour = ''
    uniqueness_by = ''
    up_scaling_policies = ''
    user_data = ''
    utilize_reserved_instances = ''
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

