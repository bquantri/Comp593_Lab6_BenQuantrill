#-----------------------------------------
# File:
# Author: Ben Quantrill
# Date: 2022/04/02
# Course: Comp593 - Scripting Applications
# Description: A script using the requests
#              module to get ability info from PokeApi and post to Pastebin
# Usage: Python .py [PokemonName]
# History: 2022/03/30 (initial creation)
#

#imported modules to allow for requests and command line parameters
import requests
from sys import argv

def main():

    poke_num = argv[1]
    poke_info = get_poke_info(poke_num)

    if poke_info:
        pastebin_message = get_pastebin_message(poke_info)
        pastebin_url = post_pastebin_message(pastebin_message[0],pastebin_message[1])
        print(pastebin_url)

def post_pastebin_message(title, body_text):
    print("Posting message to PasteBin...", end="")\

    pastebin_params = {
        "api_dev_key": "f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X",
        "api_option": "paste",
        "api_paste_code": body_text,
        "api_paste_name": title,
    }

    response = requests.post("https://pastebin.com/api/api_post.php", data = pastebin_params)

    if response.status_code == 200:
        print("congrations!")
        return response.text
    else:
        print("close, but no cigar")
        return response.status_code

def get_pastebin_message(poke_dict):

    
    title = poke_dict["name"]
    for body_text in poke_dict["abilities"]:
       print(body_text['ability']['name'])
    return (title, body_text)

def get_poke_info(poke_num):
    print("Getting Desired Pokemon abilities...", end="")
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + poke_num)

    if response.status_code == 200:
        print("congrations!")
        return response.json()
    else:
        print("close, but no cigar",response.status_code)
        return

main()
