from stringManager import *

print("Select an option:\n"+
"1. String inverter\n"+
"2. Birthday\n"+
"3. Elevate numbers\n")

while True:
  try:
    x = 0
    x = int(input("Give me a number: "))
  except:
    print("Something went wrong")

  if x == 1:
    word = input("Write a word: ")
    print(invertString(word))
  elif x == 2:
    birthday()
  elif x == 3:
    number = int(input("Give me a number to elevate: "))
    print(elevate(number, 3))
  else:
    print("Please input a correct option\n")
  
  answer = input("Finish job? (y/n): \n")
  if answer == 'y':
    break
