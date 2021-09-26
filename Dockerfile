FROM python:3.9-slim-bullseye

WORKDIR /app

COPY async_web_scraper /app/async_web_scraper
COPY requirements.txt /tmp/
COPY main.py /app

RUN pip install -r /tmp/requirements.txt

CMD ["python", "main.py"]