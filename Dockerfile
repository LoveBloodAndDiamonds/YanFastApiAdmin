FROM python:3.10.10

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

# Открытие портов
EXPOSE 80

# Запуск проекта
CMD ["uvicorn", "app.__main__:app", "--host", "0.0.0.0", "--port", "80"]
