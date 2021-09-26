# async-web-scraper
(Note: built using python 3.9)

Created a web scraping app using asnycio and aiohttp.

# Setting up

* clone repo
```
git clone https://github.com/rwtatum/async-web-scraper.git
```

* create a virtual environment and pip install requirements.txt
```
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

## Run application

```
python main.py
```

## Run tests (pytest)

```
# pip install the requirements-dev.txt
pytest tests
```

## Run on Docker

(sharing the /tmp/data directory on the host as /app/output to the container.)

```
make build
make run
```

## TODOs

1. Exception handling
2. More sophisticated storage layer
3. Improved throughput of requests
