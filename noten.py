#! /usr/bin/env python3

import requests
import json
import functools
import sys

api_key = 'OgCs72LZO52Lwk4ypLhgBenfNvEqwwbS'

def contains(list, string):
    return string in list

file = open('auth','r')
lines = file.readlines()
file.close()
sNummer = lines[0].split('\n')[0]
RZLogin = lines[1].split('\n')[0]

try:
  g = requests.post("https://wwwqis.htw-dresden.de/appservice/getcourses", data = {
       "sNummer":sNummer,
       "RZLogin":RZLogin
    }, verify = False)

  garray = json.loads(g.content.decode())

  r = requests.post("https://wwwqis.htw-dresden.de/appservice/getgrades", data = {
                        "sNummer":sNummer,
                        "RZLogin":RZLogin,
                        "AbschlNr":garray[0]["AbschlNr"],
                        "StgNr":garray[0]["StgNr"],
                        "POVersion":garray[0]["POVersion"]
                }, verify=False)

  if r.status_code == 200:
   array = json.loads(r.content.decode())
   ws14 = []
   for dic in array:
    if dic['Semester'] == '20142' and dic['PrNote'] != '':
     ws14.append(dic)

   infile = open("text","r")
   alt = json.load(infile)
   if len(alt) == len(ws14):
    print("keine neuen Noten")
    sys.exit(0)

   with open("text","w") as outfile:
     json.dump(ws14,outfile,indent=4)

   neueNoten = []
   for dic in ws14:
    if not contains(alt,dic):
     neueNoten.append(dic)

   message = functools.reduce(lambda y,x: "%s%s in %s\n" %(y,x['PrNote'],x['PrTxt']),neueNoten,"")

   headers = {'Content-Type': 'application/json', 'Authorization': "Bearer %s" %(api_key)}
   payload = {'type': 'note', 'title': message, 'body': 'Geil Mann!'}
   ret = requests.post('https://api.pushbullet.com/v2/pushes', headers = headers, data = json.dumps(payload))
   print("%s wurde an Geräte geschickt" %(message))

except requests.exceptions.RequestException as e:
            print(e)
