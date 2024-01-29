import requests
from rgbprint import *
import concurrent.futures

cookie = input("Your Cookie |~-> ")

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Cookie': cookie,
    'Sec-Ch-Ua': '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Model': '""',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Sec-Gpc': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}



current_view = 0



gradient_print(f"[1] | View Bot        [2] | Profile Clicks", start_color=Color.lime_green, end_color=Color.ghost_white)
choice = int(input("Choice |~-> "))
if choice == 1:
    url = input("Your URL |~-> ")
    amount = int(input("Amount Of Views |~-> "))
    threads = int(input("Number of Threads |~-> "))

    def make_request(_):
        global current_view 
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            gradient_print(f"{current_view} | +1 View!", start_color=Color.lime_green, end_color=Color.ghost_white)
            current_view += 1 
        else:
            gradient_print("Failed.", start_color=Color.red, end_color=Color.ghost_white)

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(make_request, range(amount))
        
elif choice == 2:
    url = input("Your URL |~-> ")
    amount = int(input("Amount Of Profile Clicks |~-> "))
    threads = int(input("Number of Threads |~-> "))

    url_id = url.split("/")[-1]

    data = {
        'url_id': url_id
    }

    def make_request(_):
        global current_view 
        response = requests.post('https://api.amitermed.com/v1/tmtry/opc', headers=headers, json=data)
        if response.status_code == 200:
            gradient_print(f"{current_view} | +1 Clicks", start_color=Color.lime_green, end_color=Color.ghost_white)
            current_view += 1
        else:
            gradient_print("Failed.", start_color=Color.red, end_color=Color.ghost_white)

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(make_request, range(amount))
