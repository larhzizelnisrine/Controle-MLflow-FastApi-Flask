FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./fastApp /app
COPY ./models app/models
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["uvicorn", "imdb_app:app", "--host", "0.0.0.0", "--port", "80"]
