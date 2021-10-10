FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY djangostagram .

CMD [ "python", "./djangostagram/manage.py", "runserver", "0.0.0.0:8000" ]

EXPOSE 8000