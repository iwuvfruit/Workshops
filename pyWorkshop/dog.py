import requests

api_url = "http://shibe.online/api/shibes?count=1"
params = {"count": 10}
response = requests.get(api_url, params = params)
#now I have 10 responses back.

status_code = response.status_code
print("status code: ", status_code)

response_json = response.json()
print(response_json)
#it will print url and it shows a url that's alive
#we just used an api 
#this library requests work with api
#other libraries do different stuff 


