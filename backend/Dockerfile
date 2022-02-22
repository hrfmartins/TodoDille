FROM python:3.8

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./ .

ENV PORT "$PORT"
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
