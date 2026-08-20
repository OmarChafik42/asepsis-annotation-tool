FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    ANNOTATION_HOST=0.0.0.0 \
    ANNOTATION_PORT=8765 \
    ANNOTATION_DATA_DIR=/data

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /data
VOLUME ["/data"]
EXPOSE 8765

CMD ["python", "run.py", "--host", "0.0.0.0", "--port", "8765", "--data-dir", "/data"]
