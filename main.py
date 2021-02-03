from madlib import start

print("Por favor seleccione una opcion:\n"+
"1. Madlib Generator\n\n")

while True:
  try:
    x = int(input("Dame un número: "))
  except:
    print("Something went wrong")

  if x == 1:
    print("Opcion 1")
    start()
    break
  else:
    print("Please input a correct option\n")
