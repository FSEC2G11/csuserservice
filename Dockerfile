FROM python:3.10.2

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/userservice

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 4001

CMD [ "python", "manage.py", "runserver", "0.0.0.0:4001" ]