from fastapi import FastAPI
import uvicorn

app = FastAPI()

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

if __name__ == "__main__":
  uvicorn.run(
      "main:app",
      host="0.0.0.0",
      port=8000,
      reload=True,
  )

