import requests

endpoint = "http://127.0.0.1:8000/api"

x = requests.get(endpoint, 
    params={'abc':"urlsparameters",},
    json={"query":"Hello World"}
    )

#print(x.text) # print raw text response
print(x.json())

print(x.status_code)


'''
HTTP Request -> HTML
REST API HTTP Request -> JSON
Javascript Object Notation ~ Python Dict
'''
