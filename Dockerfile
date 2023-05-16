FROM python:3.11.3-slim-buster
RUN apt-get update && apt-get install -y build-essential
COPY ./src ./src
COPY ./requirements.txt /src/requirements.txt
COPY ./.env /src/.env
RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]