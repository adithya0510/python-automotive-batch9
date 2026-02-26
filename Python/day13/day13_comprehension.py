#basic list comprehension - uses much memory for each element
list = [x*x for x in range(5)]
print(list)

#comprehension using generator - dont use much memory
gen=(x*x for x in range(5))
print(gen)


#dict
d = {num:num*2 for num in range(1,4)}
print(d)

states=["AP","WB","TN"]
capitals = ["Amaravathi","kolkata","Chennai"]

d1 = {states:capitals for states,capitals in zip(states,capitals)}
print(d1)

#set
a = [1,1,2,2]
s = {n for n in a if n%2==0}
print(s)