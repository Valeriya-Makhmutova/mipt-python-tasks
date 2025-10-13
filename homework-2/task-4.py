try:
  with open('homework-2/data/input.txt', 'r', encoding='utf-8') as input_file:
    line_list = []
    for line in input_file:
      if line not in line_list:
        line_list.append(line)
    
    with open('homework-2/data/unique_output.txt', 'w', encoding='utf-8') as unique_file:
      for element in line_list:
        unique_file.write(element)
except FileNotFoundError:
  print('Файл или директория не найдены. Проверьте, пожалуйста, путь до файла или директории')
except ValueError:
  print('Значение не найдено')
else:
  print('Уникальные строки успешно записаны в новый файл.')