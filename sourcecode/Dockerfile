FROM python:alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DJANGO_SUPERUSER_PASSWORD admin
ENV DJANGO_SUPERUSER_USERNAME admin
WORKDIR /app
COPY requirements.txt .
RUN apk update && apk add gcc python3-dev musl-dev mariadb-dev
RUN pip install mysqlclient
RUN pip install -r requirements.txt 
RUN apk del gcc python3-dev musl-dev
COPY . .
# CMD while ! python3 manage.py sqlflush > /dev/null 2>&1 ; do sleep 1 ; done && \
CMD python3 manage.py makemigrations --noinput && \
    python3 manage.py migrate --noinput && \
    python3 manage.py collectstatic --noinput && \
    python3 manage.py createsuperuser --user admin --noinput --email test@test.com --noinput ; \
    gunicorn -b 0.0.0.0:8000 --env DJANGO_SETTINGS_MODULE=weblog.settings --workers=6 weblog.wsgi