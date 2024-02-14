from typing import Annotated, Optional
from fastapi import FastAPI, File, Form, Response, UploadFile
from database import students
from models import Student
from fastapi.responses import StreamingResponse
from io import BytesIO

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello, World!"

# Idempotent: Methods that are safe to be retried or executed multiple times, without cuasing unintended side effects
# GET is idempotent
@app.get("/students")
def get_students(sortBy: Optional[str] = None, count: Optional[str] = None):
    def extract_field(students):
        try:
            if sortBy == "id":
                return int(students[sortBy])
            else: 
                return students[sortBy]
        except KeyError:
            return 0

    if sortBy:
        result = sorted(students, key=extract_field)
    else: 
        result = students
    if count:
        if int(count) <= 0:
            return []
        else:
            result = result if int(count) > len(students) else result[0:int(count)]
    return result


@app.post("/students")
def create_student(student: Student):
    new_student = { 
        "name": student.name,
        "id": student.id,
        "gpa": student.gpa
    }
    students.append(new_student)
    return new_student

# PUT is Idempotent
@app.put("/students")
def update_student(student: Student):
    for i in range(len(students)):
        if students[i]["id"] == student.id:
            updated_student = { 
                "name": student.name,
                "id": student.id,
                "gpa": student.gpa
            }
            students[i] = updated_student
            return students[i]
    
    create_student(student)
    return student

# DELETE is Idempotent
@app.delete("/students/{student_id}")
def delete_student(student_id: str, response: Response):
    for i in range(len(students)):
        if students[i]["id"] == int(student_id):
            students.remove(students[i])
            response.status_code = 204
            return f'{student_id} deleted successfully!'
            
    response.status_code = 404
    return "Student ID to delete not found"

'''
Challenges Implemented 

1. File upload in POST request, using multipart/form-data

2. Having a route in your application that returns a binary content type (photo, video, audio)

'''

@app.post("/file")
def save_file(file: UploadFile):
    with open(f'assets/{file.filename}', 'wb') as f:
        f.write(file.file.read())
        return "File uploaded succesfully!"

# GET is Idempotent
@app.get("/photo")
def get_binary_content():
    with open('assets/sutd.png', 'rb') as f:
        stream = BytesIO(f.read())

        return StreamingResponse(stream, media_type="image/png")
    