FROM python:3.8-slim-buster

COPY ./StockWatcher /app
RUN pip install -r /app/requirements.txt

EXPOSE 80

CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "80"]