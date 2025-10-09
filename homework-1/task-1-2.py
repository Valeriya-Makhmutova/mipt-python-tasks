# Задача 1 и 2:
def zero_devision():
  try:
      first_num = int(input('Введите первое число: '))
      second_num = int(input('Введите второе число: '))
      result = first_num / second_num
  except ZeroDivisionError:
    print('На ноль делить нельзя! Выберете другое второе число :)')
  except ValueError:
    print('Делить можно только числа! Введите, пожалуйста, числа, а не строки :)')
  else:
    if first_num % second_num == 0:
      result = int(result)
    print(f'Результат деления чисел: {result}')

zero_devision()
