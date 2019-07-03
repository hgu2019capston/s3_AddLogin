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

index = 2;
count = 0;
while True:
    if count == 10:
        break;
    x = random.choice('ABCDEFGHIJKLMNOPQRS')
    y = random.randrange(1, 20)
#    x = input("x: ")
#    y = input("y: ")

    data =  {'client': 'white','x': x, 'y': y}
    res = requests.post('http://turnincode.cafe24.com:8003/home/omok/', data = data)

    getUrl(index)
    index += 2;
    count += 1;
        

