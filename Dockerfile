FROM python:3.11.4-slim-buster AS base
RUN apt-get update && apt-get install -y build-essential libpq-dev
COPY ./src ./src
COPY ./requirements.txt /src/requirements.txt
COPY ./.env /src/.env
RUN pip install --upgrade pip
RUN pip install -U pydantic
RUN pip install psycopg2
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

FROM base as app
EXPOSE 80

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "80"]