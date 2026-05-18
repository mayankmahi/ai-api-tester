from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "AP API tester backend running"
    }