try:
  with open('homework-2/data/text_file.txt', 'r', encoding='utf-8') as text_file:
    sum_words = 0
    for line in text_file:
      word_list = line.strip().split()
      if '—' in word_list:
        word_list.remove('—')
      sum_words += len(word_list)
except FileNotFoundError:
  print('Файл или директория не найдены. Проверьте, пожалуйста, путь до файла или директории')
except ValueError:
  print('Значение не найдено')
else:
  print(f'Сумма слов в файле: {sum_words}')