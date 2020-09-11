from http.client import HTTPConnection


conn = HTTPConnection('www.baidu.com')
conn.request('GET', "/")
result = conn.getresponse()
content = result.read()
print(content)
