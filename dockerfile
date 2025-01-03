FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]
