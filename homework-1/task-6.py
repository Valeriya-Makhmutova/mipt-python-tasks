# Задача 6:
def get_sqrt():
  user_number = int(input('Введите число, корень из котрого хотите взять: '))
  try:
    import math
    result = int(math.sqrt(user_number)) if math.sqrt(user_number).is_integer() else math.sqrt(user_number)
  except ImportError:
    print('Не получилось импортировать модуль. Проверьте, пожалуйста, корректность импорта модулей')
  except NameError:
    print('Проверьте, импортировали ли вы нужный модуль')
  except ValueError:
    print('Нельзя взять корень из отрицательного числа')
  else:
    print(f'Корень из числа {user_number}: {(result)}')

get_sqrt()