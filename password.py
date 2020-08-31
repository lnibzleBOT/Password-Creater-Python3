import random
import time
import colorama
from colorama import Fore, Back, Style
import string

def menu():
    print(Fore.RED + """
    
██████╗░░█████╗░░██████╗░██████╗░░██╗██╗░█████╗░██████╗░██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝░██╔╝██║██╔══██╗██╔══██╗██╔══██╗
██████╔╝███████║╚█████╗░╚█████╗░██╔╝░██║██║░░██║██████╔╝██║░░██║
██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗███████║██║░░██║██╔══██╗██║░░██║
██║░░░░░██║░░██║██████╔╝██████╔╝╚════██║╚█████╔╝██║░░██║██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░
                            By: ImBugle#1503
                            
    """)

menu()

numofpass = int(input(Fore.GREEN + "[>] " + Fore.WHITE + "(Threads are passwords) How many threads? : "))
def numofpassTest():
    global numofpass
    numofpass += 1

numofpassTest()

print(Fore.GREEN + "[+] " + Fore.WHITE + "Creating Passwords!!")

def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    print(Fore.GREEN + "[+] " + Fore.WHITE + result_str)

for i in range(1,numofpass):
    get_random_alphanumeric_string(8)
    time.sleep(2)
else:
    print(Fore.RED + "[-] " + Fore.YELLOW + "Passwords done! you may use one.")
    print(Fore.RESET)
