import json
a = {"name":"Adithya","age":22}

#key <> value 
#first created in json file
#json - javascript object notation
#data.json

b = json.dumps(a)

#op: {"age":22,"name":"Adithya"} - json restores the data type according to the alphabetical order

with open('data.json', 'r') as file:
    data = json.load(file)
print(json.dumps(data,indent=2))  #space between the objects is 4
