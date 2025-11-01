from threading import Thread
import time

# Напишите программу,
# которая создаёт несколько потоков для выполнения функции, 
# которая выводит целые числа от 1 до 10 с задержкой в 1 секунду.
def worker() -> None:
  nums = range(1, 11)
  for num in nums:
    print(num)
    time.sleep(1)


if __name__ == "__main__":
  
  t1 = Thread(target=worker)
  t2 = Thread(target=worker)
  t3 = Thread(target=worker)

  t1.start()
  t2.start()
  t3.start()

  print("Ждём завершения потоков")

  t1.join()
  t2.join()
  t3.join()