from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
fakedb = [] #fake database 

class Course(BaseModel):
    id: int
    name: str
    price: float
    is_early_bird: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "Welcome To My Course Site"}

@app.get("/courses")
def get_courses():
    return fakedb

@app.get("/courses/{course_id}")
def get_course(course_id: int):
    return fakedb[course_id - 1] # coz array index starts from 0

@app.post("/courses")
def add_course(course: Course):
    fakedb.append(course.dict()) #add a dictionary object to the fake database
    return fakedb[-1] #display the latest object/course , last element of the data base

@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    fakedb.pop(course_id-1) 
    return {"Task": "Deletion Successful    "}