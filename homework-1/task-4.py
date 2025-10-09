# Задача 4:
def get_element_by_index(list):
  user_index = int(input('Введите индекс элемента списка: '))
  try:
    element = list[user_index]
  except IndexError:
    print('Элемент с таким индексом не существует')
  else:
    print(f"Под таким индексом находится элемент: {element}")

get_element_by_index([1, 2, 3, 4, 5, 6, 7, 8, 9])