from fastapi import FastAPI
from pydantic import BaseModel
import datetime

class TextInput(BaseModel):
    text : str

app=FastAPI()

@app.get("/")
def root():
    return {"message":"api is running"}

@app.post("/summarize/")
def summarize(data:TextInput):
    data=data.text
    word_count=len(data.split())
    hundred=data[:100]
    return {
        "Word Count":word_count,
        "Hundred": hundred
    }

@app.get("/health")
def health():
    timestamp = datetime.datetime.now()
    return {
        "status":"OK",
        "timestamp" : timestamp}
