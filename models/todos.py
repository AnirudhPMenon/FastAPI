from pydantic import BaseModel

class Todo(BaseModel):
    name: str
    college_mail: str
    reg_number: str
    password: str
    confirm_password: str
    attendance: bool

