from colorama import Fore, Back, Style, init
import urllib
import requests
from os import name, system
from time import sleep
from datetime import datetime

def Menu():
	print ("")
	print (Fore.WHITE + Style.BRIGHT + "      ____                        ________              __            ")
	print (Fore.WHITE + Style.BRIGHT + "     / __ \_________  _  ____  __/ ____/ /_  ___  _____/ /_____  _____")
	print (Fore.WHITE + Style.BRIGHT + "    / /_/ / ___/ __ \| |/_/ / / / /   / __ \/ _ \/ ___/ //_/ _ \/ ___/")
	print (Fore.WHITE + Style.BRIGHT + "   / ____/ /  / /_/ />  </ /_/ / /___/ / / /  __/ /__/ ,< /  __/ /    ")
	print (Fore.WHITE + Style.BRIGHT + "  /_/   /_/   \____/_/|_|\__, /\____/_/ /_/\___/\___/_/|_|\___/_/     ")
	print (Fore.WHITE + Style.BRIGHT + "                        /____/                                        ")
	print ("")

	target = input(" Enter a Server IP Adress to scan >> ")

	if target == "":
		print (" Please enter an IP Adress to check.")
	else:
		Check(target)

def StartupClear():
	if name == "nt":
		system("cls")
	else:
		system("clear")

def Check(targeted_server):
	try:
		print(Fore.BLUE + Style.BRIGHT + "\n [i] " + Fore.WHITE + "Checking " + targeted_server + "... \n")

		checkingurl = "https://vpn-proxy-detection.ipify.org/api/v1?apiKey=at_QcL0L1M2FXQUssiIMQVVltoho5X9V&ipAddress=" + targeted_server
		checkingfile = urllib.request.urlopen(checkingurl)

		for line in checkingfile:
			dcd_result = line.decode("utf-8")

		clean = True

		if '"proxy":false' in dcd_result:
			print(Fore.GREEN + Style.BRIGHT + " [+] " + Fore.WHITE + "No Proxy Detected")
		else:
			print(Fore.RED + Style.BRIGHT + " [-] " + Fore.WHITE + "Proxy Detected")
			clean = False

		if '"vpn":false' in dcd_result:
			print(Fore.GREEN + Style.BRIGHT + " [+] " + Fore.WHITE + "No VPN")
		else:
			print(Fore.RED + Style.BRIGHT + " [-] " + Fore.WHITE + "VPN Detected")
			clean = False

		if '"tor":false' in dcd_result:
			print(Fore.GREEN + Style.BRIGHT + " [+] " + Fore.WHITE + "No TOR Exit Node")
		else:
			print(Fore.RED + Style.BRIGHT + " [-] " + Fore.WHITE + "TOR Exit Node Detected")
			clean = False

		if(clean):
			print(Fore.BLUE + Style.BRIGHT + "\n [i] " + Fore.WHITE + targeted_server + " is " + Fore.GREEN + "clean")
		else:
			print(Fore.BLUE + Style.BRIGHT + "\n [i] " + Fore.WHITE + targeted_server + " is " + Fore.RED + "not clean")

		output = input(Fore.WHITE + Style.BRIGHT + "\n Save output as [Leave blank to skip] >> ")

		if output == "":
			print (Fore.BLUE + Style.BRIGHT + " [i] " + Fore.WHITE + "Output saving skipped.")
		else:
			try:
				print (Fore.BLUE + Style.BRIGHT + "\n [i] " + Fore.WHITE + "Saving Output as : " + output + "...")

				outputfile = open(output, "w+")

				now = datetime.now()
				datetime_s = now.strftime("%d/%m/%Y %H:%M:%S")

				outputfile.write("=============== REPORT FROM " + targeted_server + " =============== \n \n")

				outputfile.write(" [i] Scan Date : " + datetime_s + "\n \n")

				if '"proxy":false' in dcd_result:
					outputfile.write(" [+] No Proxy Detected \n")
				else:
					outputfile.write(" [-] Proxy Detected \n")

				if '"vpn":false' in dcd_result:
					outputfile.write(" [+] No VPN \n")
				else:
					outputfile.write(" [-] VPN Detected \n")

				if '"tor":false' in dcd_result:
					outputfile.write(" [+] No TOR Exit Node \n")
				else:
					outputfile.write(" [-] TOR Exit Node Detected \n")

				if(clean):
					outputfile.write("\n [i] " + targeted_server + " is clean\n")
				else:
					outputfile.write("\n [i] " + targeted_server + " is not clean\n")

				print (Fore.BLUE + Style.BRIGHT + " [i] " + Fore.WHITE + "Output succefully saved.")

			except KeyboardInterrupt:
				print (Fore.YELLOW + Style.BRIGHT + " Operation Cancelled.")
				exit()
			except:
				print (Fore.RED + Style.BRIGHT + " An error occured while saving data. \n Exiting...")
				exit()
	except KeyboardInterrupt:
		print (Fore.YELLOW + Style.BRIGHT + " Operation Cancelled.")
		exit()
	except:
		print(Fore.RED + " FATAL : Invalid IP.")
		sleep(2)
		Menu()

init(autoreset=True)
StartupClear()
Menu()