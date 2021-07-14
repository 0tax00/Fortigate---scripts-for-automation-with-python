'''
addrgrp.py

Script for adding objects to a Address Group

Mode of use:

1- Insert in the variable "member" the name of each object respecting the python syntax.
2- Insert the address group in the "grp" variable
3- After that save the script, run, take your output and just copy it to fortigate through the CLI.
'''

member = ('teste','teste')
grp = 'edit Acesso_PowerBI'
a = '"'
print(f'config firewall addrgrp \n{grp}')

for address in member: 
    print(f"\nappend member {a}{address}{a}")
print("\nend")
