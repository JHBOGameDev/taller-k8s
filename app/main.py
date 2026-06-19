from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hola desde mi microservicio!", "status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}