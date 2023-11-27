FROM python:3.9-slim
RUN apt-get update 
#--fix-missing

RUN apt install -y netcat-traditional

WORKDIR /backend
ADD ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . /backend/
WORKDIR /backend

# RUN python manage.py migrate

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"] 
