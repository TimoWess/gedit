#!/usr/bin/env python3
import requests
import os
import json

authPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./auth.json")

if not os.path.exists(authPath):
    print("No authentication file found!")
    print("Please add an auth.json file containing your username and password!")
    exit()

f = open(authPath)


data = json.load(f)

r = requests.get("https://api.github.com/users/TimoWess/gists", auth=(data["username"], data["token"]))
if r.status_code != 200:
    print("Request failed!")
    exit()

gists = []
for gist in r.json():
    gists.append(( gist['id'], list( x for x in gist['files'] )[0] ))

counter = 1
for (id, name) in gists:
    print(str(counter).zfill(2) + ": " + name + ": " + id)
    counter += 1

num = input("Please chooses a gist: ")
if not num.isnumeric():
    print("Not a number!")
    exit()

os.system('gh gist edit ' + gists[int(num)-1][0])
