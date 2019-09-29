import os
import subprocess as sb
import re
def ext_class(st):
    st = re.split('\.',st)[-1]
    st = st.replace('\'','')
    st = st.replace('>','')
    return st

def writer(ob,name):
    adhoc="ansible"
    class_name = ext_class(str(ob.__class__))
    attr = dir(ob)[26:]
    if len(ob.hosts)==0:
        allhost='all'
        adhoc = adhoc+" "+allhost+" -m "+class_name+" -a"
    else:
        allhost = ",".join(ob.hosts)
        adhoc = adhoc+" "+allhost+" -m "+class_name+" -a"
    if class_name=='command':
        print("Enter command :: ",end="")
        command_run = input()
        adhoc = adhoc+" \'"+command_run+"\'"
        return
    adhoc = adhoc+" \'"
    for x in attr:
        if x=='run' or x=='go' or x=='compile' or x=='playbook_name' or x=='hosts' or x=='register':
            continue
        else:
            attr_value = eval('ob.{}'.format(x))
            if attr_value!="":
                adhoc=adhoc+x+"="+attr_value+" "
    adhoc=adhoc+"\'"            
    return adhoc 
