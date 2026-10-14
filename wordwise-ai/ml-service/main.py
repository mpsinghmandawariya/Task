from fastapi import FastAPI
from pydantic import BaseModel,Field
from model import correct_text,predict_next_words
app=FastAPI(title="WordWise AI ML Service",version="1.0.0")
class AnalyzeRequest(BaseModel): text:str=Field(max_length=5000)
class PredictRequest(BaseModel): text:str=Field(max_length=5000); limit:int=Field(default=5,ge=1,le=10)
@app.get("/health")
def health():return {"success":True,"service":"wordwise-ml","status":"running"}
@app.post("/correct")
def correct(req:AnalyzeRequest):
 fixed,corrections=correct_text(req.text);return {"success":True,"originalText":req.text,"correctedText":fixed,"corrections":corrections}
@app.post("/predict")
def predict(req:PredictRequest):return {"success":True,"suggestions":predict_next_words(req.text,req.limit)}
@app.post("/analyze")
def analyze(req:AnalyzeRequest):
 fixed,corrections=correct_text(req.text);return {"success":True,"originalText":req.text,"correctedText":fixed,"corrections":corrections,"suggestions":predict_next_words(fixed,5)}
