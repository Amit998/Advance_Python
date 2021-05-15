import colorama
from colorama import Fore,Back,Style

colorama.init(autoreset=True)

print(Fore.RED+"hello world")
print(Fore.RESET)
print(Back.YELLOW+"hello world")


print(f"{Fore.RED}H{Fore.YELLOW}H{Fore.GREEN}H{Fore.BLUE}H{Fore.MAGENTA}H{Fore.CYAN}H   ")

print(f"{Back.YELLOW}{Fore.RED}H{Back.MAGENTA}{Fore.YELLOW}H{Back.BLACK}{Fore.GREEN}H{Fore.BLUE}H{Back.RED}{Fore.MAGENTA}H{Back.CYAN}{Fore.RED}H  ")

print(f"{Fore.RED}{Back.BLACK}{Style.BRIGHT}HELLO WORLD")