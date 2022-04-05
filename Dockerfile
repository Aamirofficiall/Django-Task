FROM python:3.10
ENV PYTHONUNBUFFERED=1
ADD . /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -U pip && pip install -r requirements.txt
EXPOSE 8000

CMD ["python","manage","runserver"]