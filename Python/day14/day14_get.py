import requests
import json

#uri : uniform resource identifier - request sender,response receiver
#url : uniform resource location - www.google().com(domain name-dns)
#json and dictionary have the same data structure

# API endpoint URL
url = "http://api.open-notify.org/astros.json"

# making the GET request --> fetch the data
response = requests.get(url)

#the data I want to post as a python dictionary

post_data={
    "":"",
    "":""
}

response1 = requests.post(url,json=post_data)
