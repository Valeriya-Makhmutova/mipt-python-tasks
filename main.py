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

# uvicorn main:app --reload main -название файла, app - переменна, где запускаем fastapi
if __name__ == "__main__":
  uvicorn.run(
      "main:app",
      host="0.0.0.0",
      port=8000,
      reload=True,
  )
