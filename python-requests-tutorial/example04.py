# import requests module
import requests

# Making a get request
response = requests.get('https://expired.badssl.com/')

# print requests object
print(response)

# passing the link to the certificate
response = requests.get('https://github.com', verify='/path/to/certifile')

# print request object
print(response)