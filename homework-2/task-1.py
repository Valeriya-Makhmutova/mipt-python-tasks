try:
  with open('homework-2/data/source.txt', 'r') as source_file:
    with open('homework-2/destination.txt', 'w') as new_file:
      for line in source_file:
        new_file.write(line)
except FileNotFoundError:
  print('Файл или директория не найдены. Проверьте, пожалуйста, путь до файла или директории')
else:
  print('Содержимое исходного файла успешно записано в новый файл')