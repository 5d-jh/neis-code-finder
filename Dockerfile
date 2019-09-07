FROM python:3.7

EXPOSE 5000

ENV PYTHONPATH /neis_code_finder/app
ENV STATIC_URL /static
ENV STATIC_PATH /neis_code_finder/app/static

WORKDIR /neis_code_finder
COPY . /neis_code_finder

RUN pip install -r requirements.txt
CMD ["uwsgi", "--ini", "uwsgi.ini"]