import requests
import time 

while True:
    response = requests.get('http://www.google.com') 
    if response.status_code != 200:
        print("Something is wrong")
    else:
        print("all good")
    time.sleep(5)
