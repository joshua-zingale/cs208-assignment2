FROM python:3.10.12

WORKDIR /usr/src/server

EXPOSE 5000

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["/bin/bash", "/usr/src/server/launch.sh"]
