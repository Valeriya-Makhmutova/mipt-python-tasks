from pydantic import BaseModel, field_validator

#Так как в задании 2 не указано, как должны работать функции - я самостоятельно спланировала их принцип работы, как смогла представить это себе.
class BookNotAvailable(Exception):
  pass

class Book(BaseModel):
  title: str
  author: str
  year: int
  available: bool
  categories: list[str]

  @field_validator("categories", mode="before")
  def categories_validator(cls, value):
    if len(value) == 0:
      raise ValueError("У книги должна быть минимум 1 категория, список не может быть пустым")
    return value
  
  def is_book_borrow(self) -> bool:
    if self.available:
      return False
    else:
      raise BookNotAvailable("Книга недоступна")


class User(BaseModel):
  name: str
  email: str
  membership_id: str

  @field_validator("email", mode="before")
  def email_validation(cls, value):
    # print('value', value)
    if "@" not in value:
      raise ValueError("Email должен содержать символ '@'")
    return value



class Library(BaseModel):
  books: list[Book]
  users: list[User]

  def total_books(self):
    books_total = 0
    for book in self.books:
      books_total += 1
    return books_total
  
  #Функция add_book скорее всего добавляет новую книгу в коллекцию библиотеки
  def add_book(self, book: Book) -> str:
    self.books.append(book)
    return "Книга успешно добавлена"
  
  def find_book(self, parameter: str, value: int | str) -> Book:
    for book in self.books:
      if getattr(book, parameter) == value:
        return f"Название искомой книги: {book.title}" 
      else:
        return "Книга не найдена"
      
  def return_book(self, book: Book) -> str:
    for element in self.books:
      if element == book:
        element.available = True
    
  

user_correct = User(name="Petya", email="petr@ya.ru", membership_id="122")
# user_error = User(name="Вася", email="vasya", membership_id="123")

war_and_peace = Book(title="war and peace", author="tolstoy", year="1867", available=True, categories=['novel'])
war_and_peace_part2 = Book(title="war and peace part2", author="tolstoy", year="1869", available=False, categories=['novel'])

first_lyb = Library(books=[ war_and_peace ], users=[ user_correct ])
print(first_lyb.add_book(war_and_peace_part2))
# print(war_and_peace.is_book_borrow())
# print(war_and_peace_part2.is_book_borrow())
# print(first_lyb.find_book("year", 1869))
