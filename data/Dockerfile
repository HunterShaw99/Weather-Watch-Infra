FROM postgres:latest AS base
RUN apt-get update && apt-get install -y
COPY ./setup/*.sql /docker-entrypoint-initdb.d/

FROM base as db
EXPOSE 8080
