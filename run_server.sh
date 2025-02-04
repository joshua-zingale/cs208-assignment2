docker network create server
docker run --rm -v ./persistent_server_storage/:/server_storage/ --network server server