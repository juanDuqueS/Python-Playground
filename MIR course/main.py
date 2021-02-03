print("Select an option:\n"+
"1. String inverter\n"+
"2. WIP\n")

def invertString(word):
  if len(word) == 0:
    return word
  else:
    return invertString(word[1:]) + word[0]

while True:
  try:
    x = int(input("Give me a number: "))
  except:
    print("Something went wrong")

  if x == 1:
    word = input("Write a word: ")
    print(invertString(word))
  elif x == 2:
    print("Option 2 not supported yet\n")
  else:
    print("Please input a correct option\n")
  
  answer = input("Finish job? (y/n): \n")
  if answer == 'y':
    break
