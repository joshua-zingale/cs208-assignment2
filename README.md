# cs208-assignment1

This is Joshua Zingale's submission code for CS208's first homework assignment. Herein is the code both for a server and a client application. The server sends a file to anyone that connects to the proper URL. The client, when run, sends two GET request to the server, one to download the checksum of the file and one to download the file; and if the downloaded checksum matches that of the downloaded file, the downloaded file is saved as "mydata_client_copy.txt", otherwise being discarded with an error message.

## Manifest

- client/
  - Dockerfile - A file that Docker can use to build an image that runs the client application
  - app.py - The client application.

- server/
  - Dockerfile - A file that Docker can use to build an image that runs the server
  - app.py - The server application
  - checksum.txt - The precomputed checksum for mydata.txt
  - mydata.txt - The file to be served
  - mydata_corrupted.txt - A file that contains data different from mydata.txt
  - requirements.txt - The python requirements for the server to work
- generate_file.py - A Python script that generate a random text file alongside its checksum, saving them in the server directory


## Usage

The server application must be started before the client can connect. Run the server application with "flask run --host 0.0.0.0". The server application broadcasts to all available interfaces all public IPs in the environment in which it is run, which may be forwarded as desired. When the server receives a GET request to the root address, mydata.txt is served; if the GET request is sent to root/checksum.txt, the checksum is served. Optionally, setting the evnironment variable "BREAK_FILE" to "TRUE" will cause the wrong file to be served from the root, without changing the checksum, to allow easy simulation of a corrupted delivery.

The client application, when run with "python app.py", sends a GET request to the address specified in the environment variable "SERVER_URL". If the variable is not set in the environment, the request is sent to "http://127.0.0.1:5000". The client first sends a GET request to SERVER_URL/checksum.txt to download checksum.txt. Then, the client sends a GET request to SERVER_URL to download mydata.txt. If either download fails or if the download checksum does not match a calculated checksum of mydata.txt, an error is printed to the standard output and the application ends. Otherwise, if the downloads occur without issue, "mydata.txt" is saved on the file system as "mydata_client_copy.txt".

To create a new pair of a random text file and a checkum, run generate_file.py, which will store them under the names "mydata.txt" and "checksum.txt" inside the server/ directory.
