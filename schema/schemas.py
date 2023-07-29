def individual_serial(todo) -> dict:
    return{
        "id" : str(todo["_id"]),
        "name" : todo["name"],
        "college_mail" : todo["college_mail"],
        "reg_number" : todo["reg_number"],
        "password" : todo["password"],
        "confirm_password" : todo["confirm_password"],
        "attendance" : todo["attendance"],
        

    }

def list_serial(todos) -> list:
    return[individual_serial(todo) for todo in todos]