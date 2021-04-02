import requests

r = requests.get("https://hyper85.github.io/Beta/")
print(r.status_code)
print(r.ok)
