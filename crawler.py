import requests
import colorama
from datetime import datetime
from colorama import Fore

colorama.init()

print(Fore.GREEN + '''
 @@@@@@@  @@@@@@@    @@@@@@   @@@  @@@  @@@  @@@       @@@@@@@@  @@@@@@@   
@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@  @@@       @@@@@@@@  @@@@@@@@  
!@@       @@!  @@@  @@!  @@@  @@!  @@!  @@!  @@!       @@!       @@!  @@@  
!@!       !@!  @!@  !@!  @!@  !@!  !@!  !@!  !@!       !@!       !@!  @!@  
!@!       @!@!!@!   @!@!@!@!  @!!  !!@  @!@  @!!       @!!!:!    @!@!!@!   
!!!       !!@!@!    !!!@!!!!  !@!  !!!  !@!  !!!       !!!!!:    !!@!@!    
:!!       !!: :!!   !!:  !!!  !!:  !!:  !!:  !!:       !!:       !!: :!!   
:!:       :!:  !:!  :!:  !:!  :!:  :!:  :!:   :!:      :!:       :!:  !:!  
 ::: :::  ::   :::  ::   :::   :::: :: :::    :: ::::   :: ::::  ::   :::  
 :: :: :   :   : :   :   : :    :: :  : :    : :: : :  : :: ::    :   : :                         
''')

bad = []
good = []

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def toString(arr):
    s = ''
    for i in range(len(arr)):
        if i > 0:
            if i == len(arr) - 1:
                s = s + ''
            else:
                s = s + ''
        s = s + arr[i];
    return s


print('\n')

url = 'https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxy-list/data.txt'
r = requests.get(url)
results = r.text
with open ('proxies.txt', 'w') as file:
    file.write(results)
    print(results)

with open('proxies.txt', 'r') as fp:
    for count, line in enumerate(fp):
        pass

print(Fore.WHITE + f'[{current_time}]' + Fore.GREEN + f'Proxies Printed: [{count+ 1}]')

checked_proxy_file = open("checked.txt", "w")
proxy_file = open('proxies.txt', 'r')
proxies = proxy_file.read()
proxies = proxies.splitlines()

for proxy in proxies:
    try:
        print(Fore.WHITE + f'[{current_time}]' + Fore.GREEN + f"Checking: " + proxy) 
        resp = (requests.get("http://google.com", proxies={"http":"http://" + proxy, "https": "https://" + proxy}, timeout=2)) 
        good.append(proxy)
        checked_proxy_file.write(toString(good))
    except requests.exceptions.ProxyError:
        bad.append(proxy)
        print(Fore.WHITE + f'[{current_time}]' + Fore.RED + f'Bad Proxy: ProxyError')
        pass
    except requests.exceptions.ConnectionError:
        bad.append(proxy)
        print(Fore.WHITE + f'[{current_time}]' + Fore.RED + f'Bad Proxy: ConnectionError')
        pass
    except requests.exceptions.Timeout:
        bad.append(proxy)
        print(Fore.WHITE + f'[{current_time}]' + Fore.RED + f'Bad Proxy: Timeout')
        pass

print(Fore.WHITE + f'[{current_time}]' + Fore.GREEN + f'Press Enter to close the program')
input()
exit()



