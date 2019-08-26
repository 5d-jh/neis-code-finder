FROM python:3

WORKDIR /usr/src/app
ADD . /usr/src/app

ENV FLASK_APP app.py
ENV FLASK_DEBUG 1

EXPOSE 5000

RUN pip install -r requirements.txt
CMD ["flask", "run", "--host=0.0.0.0"]