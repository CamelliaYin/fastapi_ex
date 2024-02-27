from fastapi import FastAPI, Path, Body
# fetch data from .env and return it with the api respose
from os import environ as env
# set some varible to be optional
from typing import Optional 
from pydantic import BaseModel

# what include in API
# - GET: get an information
# - POST: create something new
# - PUT: updated something existed
# - DELETE: delete something existed

# initialise the app 
app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "year": "year 12"
    }
}

# to create. make sure all fields are required 
class Student(BaseModel): 
    name: str
    age: int
    year: str

# to update, all fields are optional
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None 


# create the get request handler in the root endpoint: I want to show ...
@app.get("/") # this slash means we show the info at homepage 
def index():
    return {"details": f"Hello World! Secret = {env['MY_VARIABLE']}"}


# get the student info given the ID
@app.get("/get-by-id/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view", gt = 0, lt = 3)):
    return students[student_id]

# get the student info given name
@app.get("/get-by-name/{name}")
def get_student(name: str, student_id: Optional[int] = None): 
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}

# create a student with all info required
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    
    students[student_id] = student
    return students[student_id]

# update a student's partial info
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]


# use patch to update info partially, without using UpdateStudent
# this function only works for dict that follows student data structure but not the created ones.
# therefore, it can only apply patch to existed data. not recommand in use 
@app.patch("/update-student-patch/{student_id}")
def update_student(student_id: int, student: dict = Body(...)):  # Accepting a dict directly
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    existing_student = students.get(student_id)
    if 'name' in student:
        existing_student['name'] = student['name']

    if 'age' in student:
        existing_student['age'] = student['age']

    if 'year' in student:
        existing_student['year'] = student['year']

    students[student_id] = existing_student  # Update the student record
    return students[student_id]


# delete a student with all their info
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    del students[student_id]
    return {"Message": f"Student {student_id} deleted successfully"}





