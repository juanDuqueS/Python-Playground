import datetime

def invertString(word):
  if len(word) == 0:
    return word
  else:
    return invertString(word[1:]) + word[0]

def birthday():
  year = int(input("What year were you born? "))
  month = int(input("What month were you born? "))
  day = int(input("What day were you born? "))
  age = datetime.datetime.now().year - year

  print(f"Your birthday is on {day}/{month} and you are {age} years old\n")