import random
import string
import os
from register import registerObj
import writer

class na_ontap_vscan_on_demand_task:
    playbook_name = ''
    hosts=[]
    register=[]
    hostname = ''
    password = ''
    task_name = ''
    username = ''
    vserver = ''
    cross_junction = ''
    directory_recursion = ''
    file_ext_to_exclude = ''
    file_ext_to_include = ''
    http_port = ''
    https = ''
    max_file_size = ''
    ontapi = ''
    paths_to_exclude = ''
    report_directory = ''
    report_log_level = ''
    request_timeout = ''
    scan_files_with_no_ext = ''
    scan_paths = ''
    scan_priority = ''
    schedule = ''
    state = ''
    validate_certs = ''
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

