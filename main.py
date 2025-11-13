from fastapi import FastAPI, Response
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello World!"}

operators = ["+", "-", "/", "*"]
# сложение, вычитание, деление, умножение
# addition, subtraction, division, multiplication
@app.get("/addition")
async def add(a: int, b:int):
  return {"sum": a + b}

@app.get("/subtraction")
async def subtr(a: int, b:int):
  return {"result": a - b}

@app.get("/division")
async def div(a: int, b:int):
  return {"result": int(a / b)}

@app.get("/multiplication")
async def mult(a: int, b:int):
  return {"result": a * b}

@app.get("/custom_operation")
async def custom(a:int, op: str, b: int):
  if op == operators[0]:
    return {"result": f"{a} + {b} = {a + b}"}
  if op == operators[1]:
    return {"result": f"{a} - {b} = {a - b}"}
  if op == operators[2]:
    return {"result": f"{a} / {b} = {int(a / b)}"}
  if op == operators[3]:
    return {"result": f"{a} * {b} = {a * b}"}

# Требуется доработать функцию по обработке сложных выражений: сделать рекурсивную функцию 

# (а+b)* c + (d - e)/(f-g)
# (1+3)* 2 + (24 - 4)/(16-6)
# (1+3)


# @app.get("/from_str_calc")
# async def str_calc(exp: str):
#   res = {}
#   exp_no_spaces_list = list(exp.replace(" ", ""))
#   # print("exp_no_spaces_list", exp_no_spaces_list)
  
#   # (а+b)*c+(d-e)/(f-g)

#   def handl_expression():
#     result = ''
#     return result

#   for index, symb in enumerate(exp_no_spaces_list):
#     # res[index] = symb
#     # (а+b)
#     if symb == "(":
#       act_a = int(exp_no_spaces_list[index + 1])
#       act_op = str(exp_no_spaces_list[index + 2])
#       act_b = int(exp_no_spaces_list[index + 3])
#       act_res = await custom(act_a, act_op, act_b)
#       print('act_res', act_res)


#   return {"str_no_spase": exp_no_spaces_list}
#   # return res
  
# uvicorn main:app --reload main -название файла, app - переменна, где запускаем fastapi
if __name__ == "__main__":
  uvicorn.run(
      "main:app",
      host="0.0.0.0",
      port=8000,
      reload=True,
  )
