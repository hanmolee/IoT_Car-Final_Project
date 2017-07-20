import requests

URL = "http://118.91.118.27:3000/testDistance"
response = requests.get(URL)
#outdata -> List
outdata = response.json()
#dictdata -> dict
dictdata = outdata[0]
#findkey
printData = dictdata['LeftDistance']
print(printData)
