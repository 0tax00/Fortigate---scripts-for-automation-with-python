member = ('teste','teste')
grp = 'edit group_name'
a = '"'
print(f'config firewall addrgrp \n{grp}')

for address in member: 
    print(f"\nappend member {a}{address}{a}")
print("\nend")
