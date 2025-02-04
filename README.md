# cs208-assignment1

This is Joshua Zingale's submission code for CS208's second homework assignment. Herein is the code both for a server and a client application. Both applications are containerized via Docker. The server sends a file to anyone that connects to the proper URL. The client, when run, sends two GET request to the server, one to download the checksum of the file and one to download the file; and if the downloaded checksum matches that of the downloaded file, the downloaded file is saved as "mydata_client_copy.txt", otherwise being discarded with an error message.

## Manifest

- client/
  - Dockerfile - A file that Docker can use to build an image that runs the client application
  - app.py - The client application.

- server/
  - app.py - The server application
  - config.py - A configuration file for the server application
  - Dockerfile - A file that Docker can use to build an image that runs the server
  - generate_file.py - A Python script that generate a random text file alongside its checksum, saving them in the server directory
  - launch.sh - Generates random data and starts the server 
  - mydata_corrupted.txt - A file that contains data different from any possible generated mydata.txt
  - requirements.txt - The python requirements for the server to work

- compose.yaml - A docker compose file containing both the server and client, which does not fully function
- make_images.sh - Generates the client and server Docker images
- reset_env.sh - Deletes the persistent storage directories and the server's Docker network
- run_client.sh - Runs the client application once: first argument is server's IP and second is its port
- run_server.sh - Runs the server application, starting the server until the container is stopped


## Usage

Tested on Ubuntu 22.04.5 LTS.

1. Download the repository.
2. Run *make_images.sh* to create the Docker images for both the client and server applications.
3. Run *run_server.sh* to start the server application.
  - Creates a Docker network called "server", in which the server runs in a Docker container.
  - Creates a bind-mounted directory called "persistent_server_storage" in the root directory of this project with a randomly generated data file "mydata.txt" along with a file containing its checksum. This directory is available to the server's container.
4. Run *run_client.sh* to execute the client application in a Docker container.
  - The container is connected to the server network.
  - Creates a bind-mounted directory called "persistent_client_storage" in the root directory of this project. This directory is available to the client's container.
  - If the client successfully connects to the server and downloads the file, "mydata.txt" is stored in the "persistent_client_storage" directory.
5. Run *md5sum persistent_*_storage/mydata.txt* to view the checksums of both the original and downloaded file.


Note: *compose.yaml* is not fully functioning. As written, *compose.yaml* will launch both applications concurrently without ensuring that the server is accepting responses before the client sends its request.