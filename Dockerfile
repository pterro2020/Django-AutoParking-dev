FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python manage.py collectstatic --noinput && \
    python manage.py migrate --noinput && \
    gunicorn --bind 0.0.0.0:8000 autoparking.wsgi
