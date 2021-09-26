
build:
	docker build -t async_web_scraper .

run:
	docker run --rm -v /tmp/data:/app/output async_web_scraper
