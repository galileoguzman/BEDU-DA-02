import requests

response = requests.get('https://bedu.org/')
print(response)
print(response.content)