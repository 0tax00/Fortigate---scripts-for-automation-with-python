subnet = ('teste','teste')
As = '"'
print("config firewall address")
for address in subnet:
    print(f"\nedit {As}{address}{As}\nset color 18",
    f"\nset subnet {As}{address}{As}\nnext")
print("\nend")

