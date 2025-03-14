from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Cargar variables de entorno
load_dotenv(find_dotenv())

# Inicializar FastAPI
app = FastAPI()

# Inicializar modelo de IA
llm = ChatOpenAI(mo>del="gpt-4o-2024-11-20")

# Modelo de request para validar la entrada
class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "AI Service is running"}

@app.post("/chat/")
def chat(request: ChatRequest):
    try:
        response = llm.invoke([HumanMessage(content=request.message)])
        return {"response": response.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))