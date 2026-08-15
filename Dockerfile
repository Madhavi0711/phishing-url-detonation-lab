FROM python:3.12-slim

RUN pip install --no-cache-dir playwright
RUN playwright install --with-deps chromium

WORKDIR /app

COPY detonate.py .

ENTRYPOINT ["python", "detonate.py"]
