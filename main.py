import requests
from rgbprint import *
import concurrent.futures

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Cookie': 'cf_clearance=fLEa_t9vIh8WxR0eIwHJoQCMFoLOeaY0R6yZmw6ZNnA-1706483487-1-AQ8bJ2xlpan46KBcNaF7YgrHr4zrw354v2ywnb+TC0Gf6RJyolU2wD/eUwsxP1CNgWHJVtzgv1gPxEUWxK3gst8=; sb-gbsagasfzyrbrxpzambz-auth-token=%5B%22eyJhbGciOiJIUzI1NiIsImtpZCI6IlhPWHRJQmFER1JIcGc5S0siLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzA2NDg3NDM3LCJpYXQiOjE3MDY0ODM4MzcsImlzcyI6Imh0dHBzOi8vZ2JzYWdhc2Z6eXJicnhwemFtYnouc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6ImNhODk0N2NkLTkxNzItNDUyOS1iODc2LTJiYmFhYmIzYzhlMSIsImVtYWlsIjoiZ29vZGdhbWVya2FpZGVuQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmdWxsX25hbWUiOiJJZjBuIiwiaXNzIjoiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbSIsIm5hbWUiOiJJZjBuIiwicGhvbmVfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJJZi0wbiIsInByb3ZpZGVyX2lkIjoiODA1MzExNDgiLCJzdWIiOiI4MDUzMTE0OCIsInVzZXJfbmFtZSI6IklmLTBuIn0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoib2F1dGgiLCJ0aW1lc3RhbXAiOjE3MDY0ODM4Mzd9XSwic2Vzc2lvbl9pZCI6IjQ5NjIxZjVjLTE1YmYtNGQ0NS1hMmNlLWFhNGM0MWU5YTI5MSJ9.Tpb9YFr6YPizYQoCiAi0qqWEG3ZrVAUZrc-9ONB1NS8%22%2C%22G8TrA7ymvUsECGYSBeA2-A%22%2C%22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%22%2Cnull%2Cnull%5D',
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
