from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Quotation Service is running"}

@app.post("/generate_quote")
def generate_quote():
    return {"quote": "Generated quotation data"}
