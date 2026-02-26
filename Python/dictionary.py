# Dictionary - A changable, unordered, collection of unique key:value pairs
# fast because they use hashing allow us to access a value quickly

capitals = {
    'USA': 'Washington DC',
    "India": 'New Delhi',
    "China": 'Beijing',
    'Russia': 'Moscow'
}

print(capitals)
print(capitals['Russia'])
print(capitals.get("Germany"))  # None since germany is not present in the dict
print(capitals.keys())
print(capitals.values())
print(capitals.items())

# ------------------------------------------------

capitals.update({'Germany': 'Berlin'})  # adds new item pair at last position
print(capitals)
capitals.update({'USA': "Las vegas"})   # updates the value of a key
print(capitals)
capitals.pop('China')   # removes items from dict
print(capitals)
# capitals.clear()  # clears the dict

for key,value in capitals.items():
    print(key,':',value)