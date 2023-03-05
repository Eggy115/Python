import base64
a = str(base64.b64encode(b"print('hi')"))[2:]
a = a[:-1]

a = "hidden code here"

var = base64.b64decode(a)
exec(var)
