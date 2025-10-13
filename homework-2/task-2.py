try:
  with open('homework-2/data/prices.txt', 'r', encoding='utf-8') as price_file:
    sum = 0
    for line in price_file:
      list = line.strip().split()
      (name, count, price) = list
      sum += int(count) * int(price)
except FileNotFoundError:
  print('Файл или директория не найдены. Проверьте, пожалуйста, путь до файла или директории')
except TypeError:
  print('Есть проблема с типами данных')
else:
  print(f'Сумма равна: {sum} рублей')