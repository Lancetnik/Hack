FROM python:3.9
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -U pip setuptools -r requirements.txt
RUN rm requirements.txt

COPY s_requirements.txt /code/
RUN pip install --no-cache-dir -r s_requirements.txt
RUN rm s_requirements.txt

COPY /app/ /code/