Ansible module is creating ansible facts with python in library/module.py
and also fact/module  can be used by modulename, "module: value"

# module's location roles/library/module_name.py       call it as "module_name:" in playbook
# ----------------------------------------------------------------------
vi hello_world.yml:
_________________________

- hosts: localhost

  tasks:
  - name: Test that my hello_world module works
    hello_world: 
    register: result

  - debug: msg="{{ result.meta }}" 

# ----------------------------------------------------------------------

#!/usr/bin/python

from ansible.module_utils.basic import *

def main():
    module = AnsibleModule(argument_spec={})
    theReturnValue = {"hello": "world"}
    module.exit_json(changed=True, meta=theReturnValue)

if __name__ == '__main__':
    main()


#--------------------------------------------------------------------








vi version_change.yml
_____________________

- hosts: localhost

  tasks:
  - name: Test that my change_version module works
    version_change: 
      version_name: "Before"
      version_no:  1.1.1 
      unchanged_value: "This will pass through"
    register: result

  - debug: var=result                                # Note:  result contains vars from version_change: version_name, version_no etc,.
  - debug: var=test
  - debug: var=numa_nodes                            # these vars are facts, added by library "ansible_facts.update"


#---------------------------------------------------------------------
vi library/version_change.py
____________________________________

#!/usr/bin/python

from ansible.module_utils.basic import *

def main():

    fields = {
        "version_no": {"default": True, "type": "str"},
        "version_name": {"default": True, "type": "str"},
        "unchanged_value": {"default": True, "type": "str"}

    }

    module = AnsibleModule(argument_spec=fields)
    params = module.params
    # change the name
    ansible_facts = {"test": "Test_value"}
    ansible_facts.update({
        "interface_numa_cpu_lists": "cpu_lists2",
        "numa_nodes": "numa_nodes2",
        "other_numa_node_cores": "sorted(other_numa_node_cores)"
    })
    module.params.update({"version_name": "After"})
    # bump minor and patch version
    mylist = module.params["version_no"].split('.')
    mylist[2] = str(int(mylist[2]) + 2)
    mylist[1] = str(int(mylist[1]) + 1)
    mystr= '.'.join(mylist)
    module.params.update({"version_no": mystr})


    module.exit_json(changed=True, ansible_facts=ansible_facts)


if __name__ == '__main__':
    main()

# --------------------------- Practice -----------------------------------------------------------------------------------------------------------
vi test.yml    # this can be any name and any playbook to call "test" fact

- hosts: localhost

  tasks:
  - name: Test that my change_version module works
    test:   # new   ansible_fact
    register: result

  - debug: var=baldarym
  - debug: var=venera

  - name: Test Venera
    debug: msg="{{ venera }} 40 and Beka {{ baldarym.beka }} jashta"



#---------------------------------------------------------------------
vi test.py

#!/usr/bin/python

from ansible.module_utils.basic import *

def main():

    fields = {
        "baldarym": {

            "beka": 13,
            "Azat": 9,
            "Sezim": 4
        }
        
    }
   
    module = AnsibleModule(argument_spec={})
    
    fields.update({
    "venera": "ayalym"
    })    

   
    module.exit_json(changed=True, ansible_facts=fields)


if __name__ == '__main__':
    main()

# ___________________________________________________________________________________
# _________________________________ansible_facts and meta togethter__________________

vi version_change.yml
# ----------------

- hosts: localhost

  tasks:
  - name: Test that my change_version module works
    version_change:                                   # Note: 'version_change' is module, 'version_name', 'version_no' are params and argument_spec (look at py library)
      version_name: "Before"
      version_no:  1.1.1.2 
      unchanged_value: "This will pass through"
    register: result

  - debug: var=result
  - debug: var=men 

# ___________________________________________________________________________________
vi version_change.py
#----------------


#!/usr/bin/python

from ansible.module_utils.basic import *

def main():

    fields = {
        "version_no": {"default": True, "type": "str"},
        "version_name": {"default": True, "type": "str"},
        "unchanged_value": {"default": True, "type": "str"}

    }
    # params = module.params
    module = AnsibleModule(argument_spec=fields)   # look at here ^  --- add arguments as meta. Argument type: gets value from ansible playbook 

    ansible_facts = {"men": "Mirlan"}    # add ansible_facts as ansible_facts: look at next line.  these facts' values permanent and, gets calculated and set by module.py

    module.exit_json(changed=True, ansible_facts=ansible_facts, meta=module.params)


if __name__ == '__main__':
    main()
#---------------------------------------------------------------------------------------------------

