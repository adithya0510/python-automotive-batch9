players = ['dhawan','rohit','kohli','raina','rahul','dhoni','hardik','jadeja','siraj','kuldeep','bumrah']
print(players)

print(players[3])
print(players[7])

players[0] = 'gill' # updates first index value
print(players[0])

players.append("shreyas")  # add shreyas at new index from last
print(players)
players.remove('raina')  # removes player raina from the list
print(players)
players.pop()  # last element is removed
print(players)
players.pop(9)  # removes player at specific index value
print(players)
players.insert(0,"jaiswal")   # adds player at index specified
print(players)
players.sort()
print(players)

#food.clear() # clears list
for i in players:
    print(i)