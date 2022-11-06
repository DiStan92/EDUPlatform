FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /EDUPlatform
COPY poetry.lock pyproject.tml /EDUPlatform/
RUN pip install -U pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install
COPY . ./
COPY ../env ./.env
EXPOSE 8000


 docker run --name db -p 5432:5432 --env-file ./.env -d postgres:14
