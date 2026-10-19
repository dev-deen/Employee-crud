FROM python:3.11-slim

WORKDIR /app

# Prevent Python from writing pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# The build context is this project directory; preserve the app package layout.
COPY . /app/app

ENV PORT=8080

CMD exec uvicorn app.main:app --host 0.0.0.0 --port $PORT