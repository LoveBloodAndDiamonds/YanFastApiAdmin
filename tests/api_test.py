import requests

SERVER_IP: str = "5.61.46.128"  # IP сервера
API_PORT: int | str = 83  # Порт, на котором открыт API


def get_access(username: str) -> bool:
    """Функция для проверки лицензии по имени пользователя."""
    url = f"http://{SERVER_IP}:{API_PORT}/access/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        raise requests.exceptions.ConnectionError(f"Не удалось получить ответ от сервера."
                                                  f" Код: {response.status_code}")

    result: dict[str: bool] = response.json()  # Словарь формата {"access": bool}

    return result["access"]


def your_application():
    try:
        access: bool = get_access("ghoul")

        if access:
            print("Вход в программу разрешен.")
        else:
            print("Вход в программу запрещен.")
    except requests.exceptions.ConnectionError:
        print("Ошибка соединения с сервером.")
    except Exception as e:
        print(f"Неизвестная ошибка ({type(e)}) при проверке лицензии: {e}")


your_application()
