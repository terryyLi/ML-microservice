from app.predict import *
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/students/")
async def create_item(student: Student):
    student_dict = student.dict()
    result = predict(student_dict)
    is_good = int(result['good_employee'])
    return { 'good_employee': is_good }