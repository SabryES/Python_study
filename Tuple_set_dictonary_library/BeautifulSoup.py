## make web scapping easier

##Read HTMl and parsing eextracting all links 

import requests
url=requests.get("https://api.ipify.org/?format=json")
print(url.json())


