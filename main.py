from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, Karnataka 2024 Namma Kannada Namma Hemme"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    
    return {"item_id": item_id,"Hello":"yrutjt"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
