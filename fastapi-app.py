from fastapi import FastAPI
import uvicorn
from dblib.querydb import querydb

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Databricks"}

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}

@app.get("/query")
async def query():
    """Execute a SQL query"""

    result = querydb()
    return {"result": result}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')