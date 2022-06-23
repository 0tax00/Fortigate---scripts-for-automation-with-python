fqdn = ('teste','teste')
a = '"'
print("config firewall address")

for address in fqdn:
    print(f"\nedit {a}{address}{a}\nset color 18\nset type fqdn",
    f"\nset fqdn {a}{address}{a}\nnext")
print("\nend")

