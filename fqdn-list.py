'''
fqdn.py

Script to create fqdn objects.

Mode of use:

1- Insert in the variable "fqdn" the name of each object respecting the python syntax.
2- After that save the script, run, take your output and just copy it to fortigate through the CLI.

'''

fqdn = ('teste','teste')
As = '"'
print("config firewall address")

for address in fqdn:
    print(f"\nedit {As}{address}{As}\nset color 18\nset type fqdn",
    f"\nset fqdn {As}{address}{As}\nnext")
print("\nend")

