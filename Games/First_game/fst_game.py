import random
from random import randint

def rock_paper_scissors():
  print('  ' * 14, '-Камень, ножницы, бумага-\n')
  player_value = input('Введите значение: ')
  program_value = random.choice(['камень', 'ножницы', 'бумага'])
  print(program_value)
  player_value.lower
  if (player_value == 'камень' and program_value == 'ножницы') or (player_value == 'ножницы' and program_value == 'бумага') or (player_value == 'бумага' and program_value == 'камень'):
    print('Вы победили!\n\nВозврат в главное меню.\n')
  elif player_value == program_value:
    print('Ничья.\n\nВозврат в главное меню.\n')
  else:
    print('Вы проиграли.\n\nВозврат в главное меню.\n')
  mainMenu()

def guess_the_number():
  #Здесь игра "Угадай число"
  print('   ' * 11, '-Угадай число-\n')
  answer = randint(1, 11)
  #print(answer) - для проверки работает ли рандом
  player_answer = int(input('Я загадал число от 1 до 10.\nКакое число я загадал? '))
  while player_answer != answer:
    player_answer = int(input('\nНе угадал, попробуй еще раз.\n\nКакое число я загадал? '))
  print('Угадал!\nВозврат в главное меню.\n')
  mainMenu()

def mainMenu():
  #Здесь главное меню игры
  print('\n', '   ' * 10, '----------------\n','   ' * 10,'| Главное меню |\n','   ' * 10,'----------------')
  while True:
    print('   ' * 9, '1 - Камень, ножницы, бумага\n', '  ' * 13, '2 - Угадай число\n\n', '  ' * 16, end = '')
    change = input( 'Выберете игру: ')
    if int(change) == 1:
      rock_paper_scissors()
    elif int(change) == 2:
      guess_the_number()
    else:
      print('\n-Ошибка ввода, попробуйте еще раз-\n')
      continue

mainMenu()