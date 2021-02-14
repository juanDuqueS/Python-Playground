from stringManager import *

print("Select an option:\n"+
"1. String inverter\n"+
"2. Birthday\n"+
"3. Elevate numbers\n"+
"4. Name and height\n"
)

x = 0

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
  elif x == 3:
    number = int(input("Give me a number to elevate: "))
    exponent = int(input("\nGive me an exponent: "))
    print(elevate(number, exponent))
  elif x == 4:
    name = input("Give me your name: ")
    height = input("\nGive me your height: ")
    addHeight(name, height)
  else:
    print("Please input a correct option\n")
  
  answer = input("Finish job? (y/n): \n")
  if answer == 'y':
    break
