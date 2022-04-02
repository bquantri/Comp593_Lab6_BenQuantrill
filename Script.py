import requests
from sys import argv

def main():

    user_num = argv[1]
    user_info = get_user_info(user_num)
    if user_info:
        pastebin_strings = get_pastebin_strings(user_info)
        pastebin_url = post_to_pastebin(pastebin_strings[0],pastebin_strings[1])
        print(pastebin_url)



def post_to_pastebin(title, body_text):
    print("Posting to Pastebin...", end="")

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
        print("close, but no cigar",response.status_code)
        return response.status_code



def get_pastebin_strings(user_dict):


    title = user_dict["name"]
    for body_text in user_dict["abilities"]:
       print(body_text['ability']['name'])
    return (title, body_text)





def get_user_info(user_num):
    print("getting user information...", end="")
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + user_num)

    if response.status_code == 200:
        print("congrations!")
        return response.json()
    else:
        print("close, but no cigar",response.status_code)
        return


main()

