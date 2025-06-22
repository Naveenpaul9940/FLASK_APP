FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN python -m venv venv && . venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
