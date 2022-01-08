import requests
base_url = "http://127.0.0.1:5000/"

args = {
    "name": "love me like you do",
    "views": 20000,
    "likes": 9999,
}

# response = requests.put(base_url+"/video/1", params=args)
# print(response.json())
#
# input()

response = requests.get(base_url+"/video/1")
print(response.json())
