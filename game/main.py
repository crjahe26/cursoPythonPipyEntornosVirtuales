import random

def choose_options():
  options = ('piedra', 'papel', 'tijera')
  
  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()

  if not user_option in options:
    print('esa opcion no es valida')
    #continue
    return None, None

  computer_option = random.choice(options)

  print('User option =>', user_option)
  print('Computer option =>', computer_option)
  return user_option, computer_option


def check_rules(user_option, computer_option, userWins, cpuWins):
  
  
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user gano!')
      userWins += 1
    else:
      print('Papel gana a piedra')
      print('computer gano!')
      cpuWins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user gano')
      userWins += 1
    else:
      print('tijera gana a papel')
      print('computer gano!')
      cpuWins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user gano!')
      userWins += 1
    else:
      print('piedra gana a tijera')
      print('computer gano!')
      cpuWins += 1

  return userWins, cpuWins


def check_winner(userWins, cpuWins):
  if cpuWins == 2:
    print('El ganador es la computadora')
    return False
    #break
  
  if userWins == 2:
    print('El ganador es el usuario')
    return False
    #break

  return True


def run_game():
  cpuWins = 0
  userWins = 0

  rounds = 1

  game = True

  while game:
  
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
  
    print('cpuWins', cpuWins)
    print('userWins', userWins)
  
    rounds += 1
  
    user_option, computer_option = choose_options()
    userWins, cpuWins  = check_rules(user_option, computer_option, userWins, cpuWins)

    game = check_winner(userWins, cpuWins)
  
    
run_game()
