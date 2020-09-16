import socket

'''
Write a Python program to valid a IP address
'''


def test_valid_ip_address(addr):

    try:
        socket.inet_aton(addr)
        print('valid ip address')
    except socket.error:
        print('invalid ip address')


addr1 = '125.23.22.2356'
addr2 = '125.23.22.215'
test_valid_ip_address(addr1) # invalid ip address
test_valid_ip_address(addr2) # valid ip address
