FROM python:3.9.0

WORKDIR /home/


RUN git clone https://github.com/sunghak2234/do_it_django_1s.git

WORKDIR /home/django-do_it_django_1s/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD [ "python", 'manage.py', "runserver", "0.0.0.0:8000"]