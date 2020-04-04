FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

RUN pip3 install mkdocs

EXPOSE 8080

CMD ['mkdocs', 'serve']
