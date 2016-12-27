# "Persistence"

def filter_new(grades):
  with open('.known_grades', 'w+') as known_file:
    known_grades = known_file.read().splitlines()
    new_grades = []
    for grade in grades:
      if grade['PrNr'] not in known_grades:
        new_grades.append(grade)
        known_file.write(grade['PrNr'])

    return new_grades
