from pydantic import BaseModel, EmailStr

class StudentInfo(BaseModel):
    name: str
    age: int
    department: str
    year: str
    email: EmailStr