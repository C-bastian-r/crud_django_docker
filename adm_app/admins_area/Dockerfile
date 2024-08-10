FROM python:3.9.19-alpine3.20

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code

COPY . /code/

RUN pip install -r requirements.txt

CMD [ "/code/entrypoint.sh" ]
