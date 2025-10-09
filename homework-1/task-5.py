# Задача 5:
def export_string_to_float():
  user_string = input('Введите строку для преобразования в число с плавающей точкой: ')
  try:
    result = float(user_string)
  except ValueError:
    print('Такую строку преобразовать не получится, попробуйте ввести другую, не содержающую буквы')
  else:
    print(f"Результат: {result}")

export_string_to_float()