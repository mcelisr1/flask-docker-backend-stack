FROM tiangolo/uwsgi-nginx-flask:python3.6

WORKDIR /app/

RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN rm requirements.txt

COPY ./app /app

ENV STATIC_PATH /app/app/static
ENV STATIC_INDEX 1

EXPOSE 80