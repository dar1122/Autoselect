import re

a = 'asdffdas_da15.so'

if re.match('.+.so',a)!=None:
    print(1)
else:
    print(0)