
class Product():
  def __init__(self, name: str, price: float, stock: int):
    self.name = name
    self.price = price
    self.stock = stock

  def __hash__(self):
        return hash((self.name, self.price))
    
  def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price

  def update_stock(self, quantity: int):
    if quantity < 0:
      raise ValueError("Количество товара не может быть отрицательным")
    else:
      self.stock = quantity
      print("Новое количество товара успешно сохранено")


class Order():
  def __init__(self):
      self.products: dict = {} 
        
  def add_product(self, product, quantity):
    self.stock = product.stock
    self.product = product
    if self.stock < quantity:
      raise ValueError("Ошибка: Вы пытаетесь добавить количество товара большее, чем есть в наличии")
    else:
      self.products[self.product] = quantity
      product.update_stock(self.stock - quantity)
      
  def calculate_total(self):
     total = 0
     for product in self.products:
        total += product.price * self.products[product]
     return total


class Store():
  def __init__(self):
    self.products = []

  def add_product(self, product):
    self.products.append(product)
  
  def list_products(self):
    print("Список товаров магазина: ")
    for product in self.products:
      print(f"{product.name}, Цена: {product.price}, Количество: {product.stock}")
    

  def create_order(self):
     order = Order()
     return order


car = Product("Машина", 120000, 6)
table = Product("Стол", 1000, 10)

store = Store()
store.add_product(car)
store.add_product(table)

store.list_products()

order = store.create_order()

order.add_product(car, 2)
order.add_product(table, 3)

total = order.calculate_total()
print(f"Общая стоимость заказа: {total}")

store.list_products()
