'''
subnet.py

Script to create subnet objects.

Mode of use:

1- Insert in the variable "subnet" the address / mask of the object respecting the python syntax.
2- After that save the script, run it, get its output and just copy it to fortify through the CLI.
'''

subnet = ('teste','teste')
As = '"'
print("config firewall address")
for address in subnet:
    print(f"\nedit {As}{address}{As}\nset color 18",
    f"\nset subnet {As}{address}{As}\nnext")
print("\nend")
