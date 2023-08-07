import requests

# Making a GET request
r = requests.get("https://api.github.com/users/naveenkrnl")

# check status code for response received
# success code - 200
print(f"RESPONSE: {r}")

# print content of request
print(f"RESPONSE CONTENT: {r.content}")