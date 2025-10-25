FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY service/ ./service/
COPY test_app.py .

EXPOSE 5000

CMD ["python", "service/app.py"]