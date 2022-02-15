import requests
import time

def checkpac(proxyDict, pac_urls):

    for pac in pac_urls:
        print(pac)
        response =  requests.get(pac, proxies=proxyDict)
        responseText =  response.text
        splitted_file = responseText.splitlines()
        for line in splitted_file:
                print(line)
        time.sleep(2)

if __name__ == "__main__":

    pac_urls1 = [
        'http://pac.zscloud.net/riafinancial.com/ria_la.pac',
    ]


    http_proxy1  = "http://199.33.85.48:443"

    proxyDict1 = {
        "http"  : http_proxy1, 
        }

    print("*****  Welcome to pac checker  ****\n")

    
    checkpac(proxyDict1, pac_urls1,)
