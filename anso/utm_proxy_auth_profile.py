import random
import string
import os
from register import registerObj
import writer

class utm_proxy_auth_profile:
    playbook_name = ''
    hosts=[]
    register=[]
    aaa = ''
    basic_prompt = ''
    frontend_session_lifetime = ''
    frontend_session_timeout = ''
    name = ''
    utm_host = ''
    utm_token = ''
    backend_mode = ''
    backend_strip_basic_auth = ''
    backend_user_prefix = ''
    backend_user_suffix = ''
    comment = ''
    frontend_cookie = ''
    frontend_cookie_secret = ''
    frontend_form = ''
    frontend_form_template = ''
    frontend_login = ''
    frontend_logout = ''
    frontend_mode = ''
    frontend_realm = ''
    frontend_session_allow_persistency = ''
    frontend_session_lifetime_limited = ''
    frontend_session_lifetime_scope = ''
    frontend_session_timeout_enabled = ''
    frontend_session_timeout_scope = ''
    headers = ''
    logout_delegation_urls = ''
    logout_mode = ''
    redirect_to_requested_url = ''
    state = ''
    utm_port = ''
    utm_protocol = ''
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

