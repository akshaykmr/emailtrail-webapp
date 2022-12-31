FROM python:3.10.4-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip wheel && \
    pip install poetry

RUN pip install --upgrade setuptools --user

WORKDIR /usr/emailtrail
COPY poetry.lock pyproject.toml /usr/emailtrail/
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction

COPY . /usr/emailtrail/

EXPOSE 8080

CMD ["python", "run.py", "8080"]
