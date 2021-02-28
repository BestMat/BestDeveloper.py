import requests 
def getMethod(u,p):
 PARAMS = p
 r = requests.get(url = u, params = PARAMS) 
 data = r.json()
 return r
def statusCode(url):
 response = requests.get(url)
 return(response.status_code)



