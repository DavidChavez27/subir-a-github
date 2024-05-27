import random

options = ("piedra", "papel", "tijera")

rounds = 1 
computer_wins = 0
user_wins = 0


while True: 

  print("*" * 10)
  print("ROUND", rounds)
  print("*" * 10)

  print("computer_wins", computer_wins)
  print("user_wins", user_wins)

  user_option = input("piedra, papel o tijera => ")
  user_option = user_option.lower()

  rounds = rounds + 1

  if user_option not in options: 
    print("no has escogido ninguna opcion")

  computer_option = random.choice(options)

  print("User Option =>", user_option)
  print("Computer Option =>", computer_option)


  if user_option == computer_option:
    print("empate")
  elif user_option == "piedra": 
    if computer_option == "tijera":
      print("El usuario escogio tijera")
      print("ganaste")
      user_wins += 1
    else:
      print("El usuario escogio papel")
      print("usted perdio")
      computer_wins += 1
  elif user_option == "papel":
    if computer_option == "tijera":
      print("El usuario escogio tijera")
      print("usted perdio")
      computer_wins += 1
    else:  
      print("El usuario escogio piedra")
      print("usted gano")
      user_wins += 1
  elif user_option == "tijera":
    if computer_option == "piedra":
      print("El usuario escogio piedra")
      print("usted perdio")
      computer_wins += 1
    else: 
      print("El usuario escogio papel")
      print("usted gano")
      user_wins += 1

  if computer_wins == 3:
    print("computer_wins", computer_wins)
    print("user_wins", user_wins)
    print("Gano la computadora")
    break
  if user_wins == 3:
    print("computer_wins", computer_wins)
    print("user_wins", user_wins)
    print("Gano el usuario")
    break

