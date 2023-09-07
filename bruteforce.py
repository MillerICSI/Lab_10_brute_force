import requests
myguess=str(200)
for i in range(0,10000):
    response = requests.get('http://172.25.0.20/?guess='+myguess)
    currentPageText = response.text
    if "wrong" not in currentPageText:
        print(response.text)
        