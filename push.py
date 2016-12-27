from pushbullet import Pushbullet
from pushover_complete import PushoverAPI

from table import format_grade_val
from persistence import *

def send_pushover(auth, message):
  pushover = PushoverAPI(auth['api_token'])
  pushover.send_message(auth['user_key'], message)

def send_pushbullet(auth, message):
  pushbullet = Pushbullet(auth['api_key'])
  pushbullet.push_note("HTW Noten", message)

def format_push_message(grades):
  message = "Neue Noten: "

  for grade in grades:
    message += "{} in {}, ".format(format_grade_val(grade['PrNote']), grade['PrTxt'])
  return message

def send_grade_notifications(auth, grades):
  new_grades = filter_new(grades)
  if len(new_grades) < 1:
    print("Keine neuen Noten gefunden.")
    return

  message = format_push_message(new_grades)

  if 'pushover' in auth:
    send_pushover(auth['pushover'], message)
  elif 'pushbullet' in auth:
    send_pushbullet(auth['pushbullet'], message)
  else:
    print(colored("Keine Push Provider Anmeldedaten in auth.json gefunden.", 'red'))
    sys.exit(1)
