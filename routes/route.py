from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos

<<<<<<< HEAD
# @router.post("/")
# async def post_todo(todo: Todo):
#     try:
#         collection_name.insert_one(dict(todo))
#     except:
#         print("error")
    

# @router.put("/{id}")
# async def put_todos(id: str, todo: Todo):
#     collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set":dict(todo)})
=======

>>>>>>> 32b00cd703fcca20b94908fefa83cab5e16ee940
    

