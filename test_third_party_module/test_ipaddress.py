import ipaddress


def test_ipaddress():
    net = ipaddress.ip_network("10.42.115.0/24")
    # for ip in net:
    #     print(ip)
    address1 = ipaddress.ip_address('10.11.113.99')
    address2 = ipaddress.ip_address('10.42.115.99')
    print(address1 in net) # False
    print(address2 in net) # True
    inet = ipaddress.ip_interface('10.42.115.0/24')
    print(inet.network)
    print(inet.ip)



if __name__ == "__main__":
    test_ipaddress()


