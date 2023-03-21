import requests, re

data = "Hello. My email is mcintoge@mail.uc.edu Please Contact me!"
p = re.compile('[A-Za-z0-9_%.-]+[A-z0-9_%.-]+\.[A-z0-9]{2,}')
print(p.search(data).group())