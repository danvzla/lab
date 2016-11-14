Hello World
---------------
Create an inventory file
  can be named whatever you like... I suggest "inventory"
  inside file, single line with the host ip/name
  "192.168.24.2"
Create the ansible_hello_world.yml playbook
Run the Play
  ansible-playbook -i inventory ansible_hello_world.yml


Interfaces
---------------
Use the Previously Created Inventory File
Create the ansible_interfaces.yml playbook
Create the new module junos_get_interfaces.py
Run the Play
  ansible-playbook -i inventory ansible_hello_world.yml

Simple Config Changes
-------------------
Use the Previously Created Inventory File
Create the ansible_simple_config_changes.yml playbook

Templated Config Changes
-------------------------
Use the Previously Created Inventory File
Create the ansible_templated_config_changes.yml playbook
