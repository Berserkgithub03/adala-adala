# Use the official Python 3.11.5 image from the Docker Hub
FROM python:3.11.5-slim

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install system dependencies
RUN apt-get update

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app



# Set the correct WSGI application path
ENTRYPOINT ["gunicorn", "user_management.wsgi:application", "-b", "0.0.0.0:8000"]
