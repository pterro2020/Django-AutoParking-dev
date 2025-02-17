FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# Убираем сборку статики (для разработки она не нужна)
CMD python manage.py migrate --noinput && \
    python manage.py runserver 0.0.0.0:8000
