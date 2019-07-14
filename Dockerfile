FROM python:3.5.2-alpine

COPY requirements.txt ./app/
COPY FlaskQuiz ./app/
WORKDIR ./app

RUN pip install -r requirements.txt
RUN apk --no-cache add curl

EXPOSE 5000

CMD python app.py