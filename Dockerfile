FROM python:3.8-10
WORKDIR /app
COPY requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt --no-cache-dir
COPY . .
CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]
