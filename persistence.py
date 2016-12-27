# "Persistence"

from os import path

def filter_new(grades):
  if not path.isfile('.known_grades'):
    open('.known_grades', 'a').close()

  with open('.known_grades', 'r+') as known_file:
    known_grades = known_file.read().splitlines()
    new_grades = []
    for grade in grades:
      if grade['PrNr'] not in known_grades:
        new_grades.append(grade)
        known_file.write(grade['PrNr'])
        known_file.write('\n')

    return new_grades
