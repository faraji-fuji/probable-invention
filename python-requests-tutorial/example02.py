# import requests module
import requests

# Making a get request
response = requests.get("https://api.github.com")

# print request object
print(f"RESPONSE URL: {response.url}")

# print status code
print(f"RESPONSE STATUS CODE: {response.status_code}")

print(f"RESPONSE HEADERS: {response.headers}")

print(f"RESPONSE ENCODING: {response.encoding}")

print(f"RESPONSE ELAPSED: {response.elapsed}")

print(f"RESPONSE CLOSE(): {response.close()}")

print(f"RESPONSE CONTENT: {response.content}")

print(f"RESPONSE COOKIES: {response.cookies}")

print(f"RESPONSE HISTORY: {response.history}")

print(f"RESPONSE IS PERMANENT REDIRECT: {response.is_permanent_redirect}")

print(f"RESPONSE IS REDIRECT: {response.is_redirect}")

print(f"RESPONSE JSON(): {response.json()}")

print(f"RESPONSE ITER CONTENT(): {response.iter_content()}")

print(f"RESPONSE TEXT: {response.text}")

print(f"RESPONSE STATUS CODE: {response.status_code}")

print(f"RESPONSE REQUEST: {response.request}")

print(f"RESPONSE REASON: {response.reason}")

print(f"RESPONSE RAISE FOR STATUS(): {response.raise_for_status()}")

print(f"RESPONSE OK: {response.ok}")

print(f"RESPONSE LINKS: {response.links}")
