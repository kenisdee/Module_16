from fastapi import FastAPI

# Создание объекта приложения
app = FastAPI()

# Маршрут к главной странице
@app.get("/")
def get_main_page():
    return {"message": "Главная страница"}

# Маршрут к странице администратора
@app.get("/user/admin")
def get_admin_page():
    return {"message": "Вы вошли как администратор"}

# Маршрут к страницам пользователей с параметром в пути
@app.get("/user/{user_id}")
def get_user_page(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Маршрут к страницам пользователей с передачей данных в адресной строке
@app.get("/user")
def get_user_info(username: str, age: int):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}