import requests
import sys

r = requests.get("https://hyper85.github.io/Beta/")
print(r.status_code)
print(r.ok)


# new lin must be added
