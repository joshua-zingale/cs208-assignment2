from flask import Flask, send_file, Response
import os
from config import STORAGE_DIR


try:
    BREAK_FILE = os.environ['BREAK_FILE'] == "TRUE"
except:
    BREAK_FILE = False

app = Flask(__name__)

@app.route("/")
def download_file():
    if BREAK_FILE:
        return send_file(f"./mydata_corrupted.txt", as_attachment = True, download_name="mydata_client_copy.txt")
    else:
        return send_file(f"{STORAGE_DIR}/mydata.txt", as_attachment = True, download_name="mydata_client_copy.txt")

@app.route("/checksum.txt")
def download_checksum():
    return send_file(f"{STORAGE_DIR}checksum.txt", as_attachment = True)


@app.route("/status")
def status():
    return Response(status=200)