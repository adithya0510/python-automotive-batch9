#substring = slicing -> we get a substring after slicing a string
mystring = "abcdef#ghijkl"
mystring2 = "1234"
print(mystring+"m")  # string is immutable in python
sub1 = mystring[0:6]  #slice the first 7 elements
print(sub1)
sub2 = mystring[7: ]  # from 7th element till end
print(sub2)
sub3 = mystring[:5]  #first 6 elements
print(sub3)
sub4 = mystring[10]   #10th element - index from 0
print(sub4)
sub5 = mystring[-5]  #last 5 elements
print(sub5)

if "a" in mystring:
    print("a is there")

#splitting
word = mystring.split("#")
print(word)

mystring.upper()
mystring.lower()

#append is used in collections and avoided in string
mystring = mystring+"m" # string is immutable in python
print(mystring)
#the above string is not same and a new string created