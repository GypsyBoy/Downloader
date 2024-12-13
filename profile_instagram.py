import requests
import sys
from colorama import Fore,init
init()

def print_baner():
    print(Fore.GREEN+"""
 _______________________________________
|	   Profile Downloader	        |
|	   Author: Gypsyboy	        |
|	   Tel: @Xor_021		|
|	   Channel: @ArgentCrusaders0	|
|	   Github:github.com/gypsyboy	|
|_______________________________________|  
                        """)

def download_profile(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            print(Fore.GREEN+"[+] Downloading image...")
            image_response = requests.get(url)
            with open("profile_picture.jpg", "wb") as file:
                file.write(image_response.content)
            print(Fore.GREEN+"[+] Image downloaded successfully!")
        else:
            print(Fore.RED+"[-] Invalid URL or permissions issue.")
    except Exception as e:
        print(Fore.RED+"[!] Error:", e)


def main():
    print_baner()
    
    print(Fore.GREEN+"""Chose an option:
    [1]  Download 
    [99] Exit
    """)
    chosen_option = int(input("#> "))
    
    if chosen_option == 1:
        url = input("Please enter url : ")
        download_profile(url=url)
    elif chosen_option == 99:
        sys.exit("Exiting...")
    else:
        print(Fore.RED+"[!] Invalid input! \n exiting...")
        sys.exit(2)


main()