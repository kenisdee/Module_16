from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

# Маршрут к главной странице
@app.get("/")
def read_root():
    return {"message": "Главная страница"}

# Маршрут к странице администратора
@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}

# Маршрут к страницам пользователей с валидацией user_id
@app.get("/user/{user_id}")
def read_user(
    user_id: Annotated[int, Path(title="Enter User ID", ge=1, le=100)]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Маршрут к страницам пользователей с валидацией username и age
@app.get("/user/{username}/{age}")
def read_user_info(
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20)],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120)]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}