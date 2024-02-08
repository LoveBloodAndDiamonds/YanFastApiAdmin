import requests

SERVER_IP: str = "5.61.46.128"  # IP сервера
API_PORT: int | str = 83  # Порт, на котором открыт API


def get_access(username: str) -> bool:
    """Функция для проверки лицензии по имени пользователя."""
    try:
        url = f"http://{SERVER_IP}:{API_PORT}/access/{username}"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"Не удалось получить ответ от сервера. Код: {response.status_code}")

        result: dict[str: bool] = response.json()  # Словарь формата {"access": bool}

        return result["access"]
    except Exception as e:
        print(f"Ошибка при проверке лицензии: {e}")
        raise e


def your_application():
    access: bool = get_access("ghoul")

    if access:
        print("Вход в программу разрешен.")
    else:
        print("Вход в программу запрещен.")


your_application()
