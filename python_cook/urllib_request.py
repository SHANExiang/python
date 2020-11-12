from urllib import request, parse


url = "http://www.tmooc.cn/"

params = {
    'name1': 'value1',
    'name2': 'value2'
}

querystring = parse.urlencode(params)
# print(querystring)


resp = request.urlopen(url + "?" + querystring)
# print(resp.read())


resp1 = request.urlopen(url, querystring.encode('ascii'))
print(resp1.read())
