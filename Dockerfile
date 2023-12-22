FROM python:3.11

## Library: docker-compose-wait
## For more details about this tool
## https://github.com/ufoscout/docker-compose-wait

## Add the wait script to the image
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait

ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

# Expose port 8000 (or the port your Django app is running on)
EXPOSE 8000

# Command to run the Django server
CMD sh -c "\
    python manage.py makemigrations --noinput && \
    python manage.py migrate --noinput && \
    gunicorn tappy.wsgi:application --bind 0.0.0.0:8000"
