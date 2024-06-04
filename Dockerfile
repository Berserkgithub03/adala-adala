# Use the official Python 3.11.5 image from the Docker Hub
FROM python:3.11.5-slim

# Set environment variables to ensure Python runs in unbuffered and not interactive mode
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory
WORKDIR /app

# Install dependencies
# First, copy only the requirements file to leverage Docker cache
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entire project
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port that the application will run on
EXPOSE 8000

# Run Gunicorn to serve the application
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
