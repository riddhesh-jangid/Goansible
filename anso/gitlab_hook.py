import random
import string
import os
from register import registerObj
import writer

class gitlab_hook:
    playbook_name = ''
    hosts=[]
    register=[]
    hook_url = ''
    project = ''
    state = ''
    api_password = ''
    api_token = ''
    api_url = ''
    api_username = ''
    hook_validate_certs = ''
    issues_events = ''
    job_events = ''
    merge_requests_events = ''
    note_events = ''
    pipeline_events = ''
    push_events = ''
    tag_push_events = ''
    token = ''
    validate_certs = ''
    wiki_page_events = ''
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

