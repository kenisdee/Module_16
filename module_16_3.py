from fastapi import FastAPI, HTTPException, Path
from typing import Annotated

app = FastAPI()

# Инициализация словаря users
users = {
    "1": "Имя: Example, возраст: 18"
}

# GET запрос для получения всех пользователей
@app.get("/users")
def get_users():
    return users

# POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}")
def add_user(
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20)],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120)]
):
    # Находим максимальный ключ
    max_id = max(map(int, users.keys())) if users else 0
    new_id = str(max_id + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"

# PUT запрос для обновления информации о пользователе
@app.put("/user/{user_id}/{username}/{age}")
def update_user(
    user_id: Annotated[str, Path(title="User ID", min_length=1)],
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20)],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120)]
):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"

# DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}")
def delete_user(
    user_id: Annotated[str, Path(title="User ID", min_length=1)]
):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return f"User {user_id} has been deleted"