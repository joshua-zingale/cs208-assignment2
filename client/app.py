import requests
import hashlib
import os


STORAGE_DIR = "/client_storage/"

try:
    URL = os.environ['SERVER_URL']
except:
    URL = "http://127.0.0.1:5000"

# Get checksum
try:
    checksum = requests.get(f"{URL}/checksum.txt").text
except Exception as e:
    print(f"Could not download checksum:")
    raise e

# Get file
try:
    file_text = requests.get(URL).text
except Exception as e:
    print(f"Could not download file:")
    raise e

# Compare file against checksum
downloaded_checksum = hashlib.md5(str.encode(file_text)).hexdigest()
if downloaded_checksum == checksum:

    # Write file if checksum matches
    with open(f"{STORAGE_DIR}/mydata.txt", "w") as f:
        f.write(file_text)
else:
    print("Downloaded file did not match the checksome and was discarded.")
    print(f"Target MD5 checksum: {checksum}")
    print(f"Downloaded file's MD5 checksum: {downloaded_checksum}")


