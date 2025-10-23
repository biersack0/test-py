from fastapi import FastAPI
import os
import uvicorn
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hola desde Railway"}

# Definimos el modelo de datos que esperamos recibir
class TokenData(BaseModel):
    token: str

@app.post("/test")
def test(data: TokenData):
    print("Token recibido:", data.token)
    return {"received_token": data.token}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)