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
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print(Fore.WHITE + f'[{current_time}]' + Fore.GREEN + f'What type of proxy do you want(HTTP, SOCKS4, SOCKS5): ')
tp = input()
print('\n')

if(tp == 'HTTP'):
    url = 'https://api.openproxylist.xyz/http.txt'
    r = requests.get(url)
    results = r.text
    with open ('http.txt', 'w') as file:
        file.write(results)
        print(results)

    with open('http.txt', 'r') as fp:
        for count, line in enumerate(fp):
            pass

    print(Fore.WHITE + f'[{current_time}]' + Fore.GREEN + f'HTTP proxies Printed: [{count+ 1}]')

if(tp == 'SOCKS4'):
    url = 'https://api.openproxylist.xyz/socks4.txt'
    r = requests.get(url)
    results = r.text
    with open ('socks4.txt', 'w') as file:
        file.write(results)
        print(results)

    with open('socks4.txt', 'r') as fp:
        for count, line in enumerate(fp):
            pass

    print(Fore.WHITE + f'[{current_time}]' + Fore.GREEN + f'SOCKS4 proxies Printed: [{count+ 1}]')


if(tp == 'SOCKS5'):
    url = 'https://api.openproxylist.xyz/socks5.txt'
    r = requests.get(url)
    results = r.text
    with open ('socks5.txt', 'w') as file:
        file.write(results)
        print(results)

    with open('socks5.txt', 'r') as fp:
        for count, line in enumerate(fp):
            pass

    print(Fore.WHITE + f'[{current_time}]' + Fore.GREEN + f'SOCKS5 proxies Printed: [{count+ 1}]')

print(Fore.WHITE + f'[{current_time}]' + Fore.GREEN + f'Press Enter to close the program')
input()
exit()



