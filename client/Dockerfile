FROM python:3.10.12

WORKDIR /usr/src/client

RUN pip install requests

EXPOSE 5555

COPY . .

CMD ["python3", "app.py"]
