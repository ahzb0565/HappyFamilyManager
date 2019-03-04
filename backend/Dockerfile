FROM python:3

VOLUME /data

WORKDIR ./app

COPY . .

RUN pip3 install --no-cache-dir -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com -r requirements.txt

ENTRYPOINT ["bash", "./entrypoint.sh"]

EXPOSE 8000