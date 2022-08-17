# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster as build
WORKDIR /app
COPY . .

FROM build as unit-tests
COPY requirements-dev.txt ./
RUN pip3 install -r requirements-dev.txt && \
    pip3 install -e .
RUN pytest -k unit

FROM build as lint
RUN pip3 install flake8
RUN flake8 pc_status tests --ignore=E501 --show-source --statistics

FROM build as e2e-test
COPY requirements.txt ./
ENV FLASK_APP=pc_status
RUN pip3 install -r requirements.txt
RUN pip3 install .
RUN flask init-db && flask init-test-data
CMD gunicorn --bind 0.0.0.0:$PORT 'pc_status:create_app()'

FROM build
COPY requirements.txt ./
ENV FLASK_APP=pc_status
RUN pip3 install -r requirements.txt
RUN pip3 install .
RUN flask init-db
CMD gunicorn --bind 0.0.0.0:$PORT 'pc_status:create_app()'
