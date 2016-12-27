#! /usr/bin/env python

import sys
import json

import requests

from table import *
from push import *

# Auth

def load_auth():
  with open('auth.json', 'r') as authfile:
    try:
      authfile = open('auth.json','r')
    except FileNotFoundError:
      print(colored("Es existiert keine Datei namens auth.json im aktuellen Verzeichnis.", 'red'))
      print(colored("Benenne bitte auth_example.json um und fülle die passenden Felder aus.", 'red'))
      sys.exit(1)

    auth = json.loads(authfile.read())

    if 'login' not in auth or 'password' not in auth:
      print(colored("Bitte stelle sicher, dass sowohl das Feld 'login' als auch das Feld 'passwort' in auth.json vorhanden sind.", 'red'))
      sys.exit(1)

    if not auth['login'] or not auth['password']:
      print(colored("Bitte hinterlege in der auth.json einen Login (sNummer) und ein Passwort.", 'red'))
      sys.exit(1)

    return auth

# API

def get_grades(login, password):
  courses_request = requests.post('https://wwwqis.htw-dresden.de/appservice/getcourses', data = {
                                    'sNummer': login,
                                    'RZLogin': password
                                  })
  courses = json.loads(courses_request.content.decode())

  grades_request = requests.post('https://wwwqis.htw-dresden.de/appservice/getgrades', data = {
                                  'sNummer': login,
                                  'RZLogin': password,
                                  'AbschlNr': courses[0]['AbschlNr'],
                                  'StgNr': courses[0]['StgNr'],
                                  'POVersion': courses[0]['POVersion']
                                 })
  return json.loads(grades_request.content.decode())




def main():
  auth = load_auth()
  grades = get_grades(auth['login'], auth['password'])

  args = sys.argv[1:]
  if '-p' in args or '--push' in args:
    send_grade_notifications(auth, grades)

  table = generate_table(grades)
  print_table(table)

if __name__ == '__main__':
  main()
