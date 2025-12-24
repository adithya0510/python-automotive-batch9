# default method
# mylist = []

# if 2 in mylist:

# else:


import re
s = "h e l l o"
i = "e"
res=re.search(i,s)  # search pattern

if res:
    print("True")
else:
    print("False")