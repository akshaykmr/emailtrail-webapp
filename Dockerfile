FROM python:3.10.4-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PORT=8080

RUN pip install --upgrade pip wheel && \
    pip install poetry

RUN pip install --upgrade setuptools --user

WORKDIR /usr/emailtrail
COPY poetry.lock pyproject.toml /usr/emailtrail/
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction

COPY . /usr/emailtrail/

CMD ["sh", "-c", "python run.py $PORT"]
