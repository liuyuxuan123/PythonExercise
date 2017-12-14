
aStr = 'liuyuxan'

print('chr()',chr(65))
print('ord()',ord('A'))
print('hex()',hex(100))
print('oct()',oct(100))

print('count()',aStr.count('*'))
print('endswith()',aStr.endswith('an'))
print('startswith()',aStr.startswith('liu'))

aStr = aStr + '\t'
print('expandtabs()',aStr.expandtabs(10))

print('find()',aStr.find('u'))
print('replace()',aStr.replace('u','*'))

print('isdigit()',aStr.isdigit())
print('isalnum()',aStr.isalnum())
print('isalpha()',aStr.isalpha())
print('istitle()',aStr.istitle())
print('isspace()',aStr.isspace())
print('islower()',aStr.islower())
print('isupper()',aStr.isupper())
print('swapcase()',aStr.swapcase())
print('capitalize()',aStr.capitalize())

print('center()',aStr.center(20))
print('ljust()',aStr.ljust(20))
print('rjust()',aStr.rjust(20))

print('strip()',aStr.strip())
print('lstrip()',aStr.lstrip())
print('rstrip()',aStr.rstrip())
aStr = 'This*is*my*name:*liuyuxuan'
print('split()',aStr.split('*'))
print('join()',' '.join(aStr.split('*')))







