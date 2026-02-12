from fastapi import FastAPI, Depends
from database import engine, session

import schemas
import models
from sqlalchemy.orm import Session




# create db tables
models.Base.metadata.create_all(bind = engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

# create a students-info
@app.post("/students")
def create_students(student: schemas.StudentInfo, db: Session = Depends(get_db)):
    db_student = models.StudentInfo(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
    

# see all students
@app.get("/students")
def get_all_students(db: Session = Depends(get_db)):
    return db.query(models.StudentInfo).all()

# see students by id
@app.get("/students/{id}")
def get_student_by_id(id: int, db: Session = Depends(get_db)):
    db_student = db.query(models.StudentInfo).filter(models.StudentInfo.id == id).first()
    if db_student:
        return db_student
    return "Student Not found"

# update students by id
@app.patch("/students/{id}")
def update_student(id: int, student: schemas.StudentInfo, db:Session = Depends(get_db)):
    db_student = db.query(models.StudentInfo).filter(models.StudentInfo.id == id).first()
    if db_student:
        db_student.name = student.name
        db_student.age = student.age
        db_student.department = student.department
        db_student.year = student.year
        db_student.email = student.email
        db.commit()
        db.refresh(db_student)
        return db_student
    
    return "Student not found"

# delete student
@app.delete("/students/{id}")
def delete_student(id: int, db: Session = Depends(get_db)):
    db_student = db.query(models.StudentInfo).filter(models.StudentInfo.id == id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
        return "Student Deleted"
    
    return "Student not found"


