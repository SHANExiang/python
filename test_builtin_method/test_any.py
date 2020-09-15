
'''
Write a Python program to check whether lowercase letters exist in a string.
'''


def test_any():
    st = 'A8238i823acdeOUEI'
    print(any(x.islower() for x in st))
    st = 'DGRFRHR354DGHRYJH'
    print(any(x.islower() for x in st))


test_any()
# True
# False
