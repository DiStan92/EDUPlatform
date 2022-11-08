FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /EDUPlatform
COPY poetry.lock pyproject.toml /EDUPlatform/
RUN pip install -U pip && \
   pip install poetry && \
   poetry config virtualenvs.create false && \
   poetry install
COPY . ./
COPY ../.env ./.env
EXPOSE 8000
ENTRYPOINT ["bash", "-c", "/EDUPlatform/entrypoint.sh"]
