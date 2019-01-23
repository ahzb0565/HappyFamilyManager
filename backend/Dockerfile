FROM python:3

VOLUME /data

WORKDIR ./app

COPY . .

RUN pip3 install --no-cache-dir -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com -r requirements.txt

CMD [ "python3", "./manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000