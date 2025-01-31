FROM python:3.10.12

WORKDIR /usr/src/server

EXPOSE 5000

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "python3 generate_file.py && flask run --host=0.0.0.0"]
