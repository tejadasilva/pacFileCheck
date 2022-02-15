import requests
import time

def checkpac(proxyDict, pac_urls, str_to_check ):

    for pac in pac_urls:
        print(pac)
        response =  requests.get(pac, proxies=proxyDict)
        responseText =  response.text
        splitted_file = responseText.splitlines()
        for line in splitted_file:
            check_line =  line.find(str_to_check)
            if check_line > 0:
                print(line)
                continue
        time.sleep(2)

if __name__ == "__main__":

    with open('list1.txt') as file1:
        pac_urls1=file1.readlines()

    with open('list2.txt') as file2:
        pac_urls2=file2.readlines()



    http_proxy1  = "http://199.33.85.48:443"
    http_proxy2  = "http://199.33.87.48:443"


    proxyDict1 = {
        "http"  : http_proxy1, 
        }
    proxyDict2 = {       
        "http"  : http_proxy2, 
        }

    str_to_check='199.33.8'

    print("*****  Welcome to pac checker  ****\n")

    
    checkpac(proxyDict1, pac_urls1, str_to_check)
    checkpac(proxyDict2, pac_urls2, str_to_check)