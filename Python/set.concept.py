myset ={"apple","banana","pomegranate","apple",False,0,2}
mylist = ['a','b']
myset2 = {"m","n"}
print(mylist)
empty_set = set()
empty_dict = {}
print(type(empty_set))  #gives datatype 

# Set operations

#mylist.add(10)
mylist.discard(10)
myset.update(mylist)
mylist.append("grapes")
count = len(myset)

print(myset|myset2)  #union
print(myset&myset2)  #intersection

for fruit in myset:
    print(fruit)
#true = 1 (duplicate)
#false = 0

# in keyword -> checks if subset present in whole set or not
# lhs of in is subset of rhs of in
'banana' in myset  #true(bool)
'grapes' in myset  #false(bool)