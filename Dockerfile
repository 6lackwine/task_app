FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt


COPY tasks/ ./tasks/

RUN python tasks/manage.py makemigrations
RUN python tasks/manage.py migrate

CMD ["python", "tasks/manage.py", "runserver", "0.0.0.0:8000"]
