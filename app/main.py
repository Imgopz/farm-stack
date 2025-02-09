from fastapi import FastAPI

app = FastAPI(title="FastAPI Backend")

@app.get('/')
def read_root():
    return {"message": "Welcome to FastAPI Backend"}
