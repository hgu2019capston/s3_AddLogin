import requests, json
import time
import random

def getUrl(index):
    url = 'http://turnincode.cafe24.com:8003/home/omok/'+str(index)+'/'
    res = requests.get(url)
    if res.status_code == 404:
        time.sleep(5)
        getUrl(index)
    else:
        print(res.text)

index = 1;
count = 0;
while True:
    getUrl(index)
   
    if count == 10:
        break;

    x = random.choice('ABCDEFGHIJKLMNOPQRS')
    y = random.randrange(1, 20)

    data =  {'client': 'black','x': x, 'y': y}
    res = requests.post('http://turnincode.cafe24.com:8003/home/omok/', data = data)

    index += 2;
    count += 1;
        

