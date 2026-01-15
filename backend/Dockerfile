FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_ENV=production
ENV PYTHONPATH=/app
CMD ["sh", "-c", "python -m gunicorn run:app -b 0.0.0.0:${PORT:-8000} --timeout 120 --workers 4"]