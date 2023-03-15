import base64
# encode code
a = str(base64.b64encode(b"print('hi')"))[2:]
a = a[:-1]
#decode code here
a = "hidden code here" # add your own encoded code here
var = base64.b64decode(a)
exec(var)
# can be used with base85, 32, 16 etc.
