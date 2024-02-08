import datetime

from fastapi import FastAPI
from sqladmin import Admin, ModelView
import uvicorn

from app.db import User, session_maker, engine
from app.auth import AdminAuth
from app.config import Config, logger

app = FastAPI()

admin_auth = AdminAuth(secret_key=Config.CYPHER_KEY)

admin = Admin(app, engine, authentication_backend=admin_auth)


@app.get('/access/{username}')
async def access(username: str):
    """
    Возвращает пользоватлю типовый словарь:
    {"access": bool,  # True если текущая дата < чем дата истечения подписки}
    :param username:  Имя пользователя
    :return:

    exmaple:
    import requests
    license_key = "your_license_key"
    url = f"http://your_api_url/access/{username}"
    response = requests.get(url)
    data = response.json()
    """
    try:
        logger.info(f"New access request with {username=}.")
        with session_maker() as session:
            user: User | None = session.query(User).filter(User.username == username).first()
        logger.info(f"{username=} is {user}")

        # Если юзер не был найден в базе данных
        if not user:
            logger.info(f"Returning False to {username}")
            return {"access": False}

        else:
            # Если срок истечения подписки больше, чем текущее время
            if user.expired_date > datetime.datetime.now().date():
                logger.info(f"Returning True to {username}")
                return {"access": True}
            # Если срок истченеия подписки меньше, чем текущее время
            else:
                logger.info(f"Returning False to {username}")
                return {"access": False}

    except Exception as e:
        logger.exception(e)


class UserAdmin(ModelView, model=User):
    """Модель отображения админки для sqladmin"""
    column_list = [User.username, User.expired_date]
    column_sortable_list = [User.username, User.expired_date]
    column_searchable_list = [User.username, User.expired_date]


admin.add_view(UserAdmin)
