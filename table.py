from terminaltables import AsciiTable
from termcolor import colored

def format_grade_val(grade):
  grade = float(grade)
  return grade / 100

def format_semester(semester_str):
  year = semester_str[:4]
  semester_id = semester_str[-1]
  if semester_id is "1":
    semester_id = 'SS'
  else:
    semester_id = 'WS'
  return "{} {}".format(semester_id, year)



def grade_color(grade):
  if grade < 4:
    return 'green'
  elif grade == 4:
    return 'yellow'
  else:
    return 'red'

def grade_to_arr(grade):
  grade_val = format_grade_val(grade['grade'])
  color = grade_color(grade_val)
  grade = [
    format_semester(str(grade['semester'])),
    grade['examDate'],
    grade['text'],
    grade['credits'],
    grade['form'],
    grade['tries'],
    colored(str(grade_val), color),
    colored(grade['state'], color)
  ]

  return grade

def generate_table(grades):
  table = [['Semester', 'Datum', 'Pruefung', 'Credits', 'Form', 'Versuch', 'Note', 'Status']]
  for grade in grades:
    table.append(grade_to_arr(grade))
  return table

def print_table(table):
  table = AsciiTable(table)
  print(table.table)
