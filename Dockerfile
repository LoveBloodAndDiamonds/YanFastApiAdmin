FROM python:3.10.10

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

# Открытие портов
EXPOSE 80

# Запуск проекта
CMD ["uvicorn", "src.admin.main:app", "--host", "0.0.0.0", "--port", "80"]
