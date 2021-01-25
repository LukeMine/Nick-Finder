import requests

import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Fore.GREEN + '''
 /$$   /$$ /$$           /$$                                                   /$$$$$$$$ /$$                 /$$                    
| $$$ | $$|__/          | $$                                                  | $$_____/|__/                | $$                    
| $$$$| $$ /$$  /$$$$$$$| $$   /$$ /$$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$ | $$       /$$ /$$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$ 
| $$ $$ $$| $$ /$$_____/| $$  /$$/| $$__  $$ |____  $$| $$_  $$_  $$ /$$__  $$| $$$$$   | $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$  $$$$| $$| $$      | $$$$$$/ | $$  \ $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$| $$__/   | $$| $$  \ $$| $$  | $$| $$$$$$$$| $$  \__/
| $$\  $$$| $$| $$      | $$_  $$ | $$  | $$ /$$__  $$| $$ | $$ | $$| $$_____/| $$      | $$| $$  | $$| $$  | $$| $$_____/| $$      
| $$ \  $$| $$|  $$$$$$$| $$ \  $$| $$  | $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$| $$      | $$| $$  | $$|  $$$$$$$|  $$$$$$$| $$      
|__/  \__/|__/ \_______/|__/  \__/|__/  |__/ \_______/|__/ |__/ |__/ \_______/|__/      |__/|__/  |__/ \_______/ \_______/|__/      
''')
print('''..........................................................................Coded By $GodBlessYou#0606.....................................................''')
                                                                             
nick = input("Enter User | Ingresa usuario: ")






def osint(list):
	file = open(list) 


	for line in file:
		name = line.split(' ')[0]
		site = line.split(' ')[1]
		
		
		
		site = site.rstrip("\n")
		url = site + nick
		
		
		
		try:
			r = requests.get(url)
	
			if r.status_code == 200:

				print(Fore.GREEN + "found " + name + ": " + url)
			else:
				print(Fore.RED + name + " not found")
		except:
			print(Fore.YELLOW + "request error for " + name)

	file.close()

print(Fore.WHITE + "Social Networks")
osint("snm.txt")

print(Fore.WHITE + "VideoHosting:")
osint("vh.txt")

print(Fore.WHITE + "GameSites:")
osint("games.txt")


print(Fore.WHITE + "Forums: ")
osint("forums.txt")

print(Fore.WHITE + "Money: ")
osint("money.txt")

print(Fore.WHITE + "Extra Sites: ")
osint("other.txt")