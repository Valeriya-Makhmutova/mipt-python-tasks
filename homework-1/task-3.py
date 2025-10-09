# Задача 3
class EvenNumber(Exception):
      pass
class NegativeNumber(Exception):
      pass

def list_sum(list_number):

  result = 0
  for number in list_number:
    # print('number', number)
    if number % 2 == 0:
      raise EvenNumber('В списке не должно быть чётных чисел')
    elif number < 0:
      raise NegativeNumber('В списке не должно быть отрицательных чисел')
    else:
      result += number
    
  return result
    
try:
# вставить спико для проверки нужно тут 
  sum_result = list_sum([1, 3, 5, 7])
except EvenNumber as e:
   print(e)
except NegativeNumber as e2:
   print(e2)
else:
   print(f"Результат сложения чисел списка: {sum_result}")


# список для проверки с четным числом [1, 2, 3, 4]
# список для проверки с отрицательным числом [1, -5, 5]
# список для проверки правильный [1, 3, 5, 7]