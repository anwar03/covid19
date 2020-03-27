FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /covid19
WORKDIR /covid19
ADD . /covid19/
RUN pip install -r requirements.txt
