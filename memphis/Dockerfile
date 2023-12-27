FROM python:3.11

ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY ./ /app/

ENV PYTHONPATH="${PYTHONPATH}:/app"
CMD ["python", "memphis/consumer.py"]
