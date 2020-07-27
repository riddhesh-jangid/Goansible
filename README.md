# Goansible :scroll:

Goansible compiles python programs into ansible commands and execute them :computer:

## Install Httpd on all server

```
from anso.package import package
task = package()
task.name = "httpd"
task.state = "present"
task.go()
```

That's it...You don't need to write any playbook. There are four main steps for automate with goansible

> 1. Import module 
> 2. Declare object of that module
> 3. Set attributes
> 4. Call go function

***You need to open python interpreter in the same directory of goansible***
***You don't need to setup goasnible when you clone from here. Direct use goansible after download***

#### 1 Import Module
Name of module is same as name of module in ansible. Importing is easy we need to import module from anso like:

*from anso.module_name import module_name*

#### 2 Declare object 

*object_name = module_name()*

#### 3 Set attributes
Attributes of module is also same as in ansible. Attributes are data members of class so we can set them like:

*object_name.attribute_name = "value"*

#### 4 Call go function

*object_name.go()*

## Variables,Loops and conditions
We can use python's variables,loops and conditions in goansible. Let we want to add users from a list

```
user_list = ['ben','gwen','kevin','vilgax']
from anso.user import user
adduser_task = user()
adduser_task.shell = "/bin/bash"
adduser_task.state = "present"
for name in user_list:
    adduser_task.name = name
    adduser_task.go()
```

## How to check status task/object
Every object have a extra varibale called register. We can check status of last running task by its register attribute

*print(obejct_name.register)*

register is a list so we can also extract value from register for further procedure. If we want to extract information 
about 4th node we need to access object_name.register[4]. Information about any node is save in form of dictionary 
so we can easily extract information by keys.

## How to update hosts list
By default hosts list is set to ALL but we can modify it by appending in it. Suppose we want that our task is run 
on only on two IPs 172.17.0.2 and 172.17.0.3

*object_name.hosts.append("172.17.0.2")* <br/> 
*object_name.hosts.append("172.17.0.3")*

                 or
                 
*object_name.hosts = ["172.17.0.2","172.17.0.3"]*  

## How to find module for any any task

```
from suggest import search_module
print(search_module("start service"))
print(search_module("Install httpd"))
```

## Possibility in goansible
1 We can use powerfull python libraries while automate<br/>
2 More comfortable for core python developer<br/>
3 Can be a fast debugging tool because we can operate it on python interpreter<br/>
4 Modularity and reusability in code<br/>
5 We can develop GUI for different purpose using tkinter,PyGTK etc.<br/>

## Files Structure

--ansible.cfg [ansible configuration file]<br/>
|<br/>
--compulsery [Directory] [Files carry compulsery attributes of every module] [Used in setup]<br/>
|<br/>
--hosts [ansible host file]<br/>
|<br/>
--setup2.py [Used in setup]<br/>
|<br/>
--suggest.py [Suggest which module to use for any task]<br/>
|<br/>
--writer.py [writer of goansible]<br/>
|<br/>
--anso [Director] [Contains classes of all modules] [Used for writer]<br/>
|<br/>
--dictionary [List of all modules] [Used in setup]<br/>
|<br/>
--others [Directory] [Files carry other then compulsery attributes] [Used in setup]<br/>
|<br/>
--register.py [Insert values in register variable]<br/>
|<br/>
--setup.py [Used in setup]<br/>

## Extension of goansible
This project is a prototype and have possibilities of extension in so many ways. 
