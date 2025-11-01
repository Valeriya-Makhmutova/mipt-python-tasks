from threading import Thread

# Напишите программу, 
# которая создаёт 2 потока для вычисления квадратов и кубов целых чисел от 1 до 10.
def worker(name: str) -> None:
  list_result = []
  list_numbers = range(1, 11)

  while True:
    if (name == "sqrt"):
      for num in list_numbers:
        list_result.append(num ** 2)
      task_name = f"Возведение чисел от 1 до 10 в квадрат: {list_result}"
      print(task_name)
      break

    if name == "cube":
      for num in list_numbers:
        list_result.append(num ** 3)
      task_name = f"Возведение чисел от 1 до 10 в куб: {list_result}"
      print(task_name)
      break

if __name__ == "__main__":
  t1 = Thread(target=worker, args=("sqrt",))
  t2 = Thread(target=worker, args=("cube",))

  t1.start()
  t2.start()

  print('Ждем завершения')

  t1.join()
  t2.join()