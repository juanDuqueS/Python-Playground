from stringManager import *

print("Select an option:\n"+
"1. String inverter\n"+
"2. WIP\n")

while True:
  try:
    x = int(input("Give me a number: "))
  except:
    print("Something went wrong")

  if x == 1:
    word = input("Write a word: ")
    print(invertString(word))
  elif x == 2:
    birthday()
  else:
    print("Please input a correct option\n")
  
  answer = input("Finish job? (y/n): \n")
  if answer == 'y':
    break
