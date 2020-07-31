import os
import sys
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore
init()
dirname = sys.argv[1]
if not os.path.exists(dirname) :
    os.mkdir(dirname)
while True:
    url = input()
    if url == 'exit':
        sys.exit(0)
    if '.' in url:
        if 'http' not in url:
            url = 'https://' + url
        r = requests.get(url)
        soup = BeautifulSoup(r.content,'html.parser')
        filename = url.replace("https://", "")
        filename = filename.replace(".com", "")
        try:
            filename = filename.replace(filename[filename.index('/'):],"")
        except ValueError:
            pass
        filename = filename + '.txt'
        with open(dirname + '/' + filename, 'w') as file:
            for item in soup.find_all(['p', 'header', 'a', 'ul', 'ol', 'li']):

                print(Fore.BLUE + item.getText())  # incomplete

                file.write(item.getText())
    else:
        try:
            with open(dirname + '/' + url + '.txt', 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("Error: Incorrect URL")
# history = []
# historyplus = []
# while True:
#     historyplus = history[:-1]
#     user = input()
#     if user == 'exit':
#         break
#     userm = user.split('.')[0] + '_com'
#     if '.' in user:
#         loc = dirname + '/' + user[:user.index('.')] + ".txt"
#         if userm == "nytimes_com":
#             with open(loc, 'w') as file:
#                 file.write(nytimes_com)
#             history.append(userm)
#             print(nytimes_com)
#         elif userm == "bloomberg_com":
#             with open(loc, 'w') as file:
#                 file.write(bloomberg_com)
#             history.append(userm)
#             print(bloomberg_com)
#         else:
#             print("Error: Incorrect URL")
#     elif user == "back":
#         try:
#             history.pop()
#             print(websites.get(historyplus.pop()))
#         except IndexError:
#             print()
#     else:
#         try:
#             loc = dirname + '/' + user + '.txt'
#             with open(loc, 'r') as file:
#                 print(file.read())
#         except:
#             print("Error: Incorrect URL")
