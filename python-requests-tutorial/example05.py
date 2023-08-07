# import requests module
import requests

# create a session object
s = requests.Session()

# again make a get request
s.get('https://httpbin.org/cookies/set/sessioncokie/123456789')

# again make a get request
r = s.get('https://httpbin.org/cookies')

# check of cookie is still set
print(r.text)