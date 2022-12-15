import requests

response = requests.get('https://httpbin.org/get')

# get status code
print(response.status_code)

res_json = response.json()

# the origin field contains the IP Address of a user, - delete that if you're pasting a screenshot or something
print(res_json) 

