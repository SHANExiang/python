import ipaddress


net = ipaddress.ip_network('10.42.115.24/20', False)
print(net.netmask)
for x in net:
    print(x)

# 01110011
# 00011000
