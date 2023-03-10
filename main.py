import requests

response = requests.get('https://httpbin.org/get')

# get status code
print(response.status_code)
res_json = response.json()

# the origin field contains the IP Address of a user, - delete that if you're pasting a screenshot or something
print(res_json) 

payload = {
    'name' : 'Ahmad',
    'age' : 21,
}

# Send a post request
response_post = requests.post('https://httpbin.org/post', data=payload)
res_json_post = response_post.json()
print(res_json_post)

# Chaing user-agent - using headers (Default user agent is python requests)
headers = {
    'User-Agent' : 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
    'Accept' : 'image/png',
}
res = requests.get('https://httpbin.org/user-agent', headers=headers)
print(res.text)

# Getting images
res_img = requests.get('https://httpbin.org/image', headers=headers)
with open('myimage.png', 'wb') as f:
    f.write(res_img.content)
    
    
# Proxies and rotating IPs
proxies = {
    'http' : '139.99.237.62:80',
    'https' : '139.99.237.62:80',
}
res_prox = requests.get('http://httpbin.org/get', proxies=proxies)
print(res_prox.text)