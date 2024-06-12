# Setup Chroma DB in Docker
Chroma is a open-source embedding database.

## Clone the repo
    git clone https://github.com/chroma-core/chroma.git

## Run the docker compose file
    cd chroma
    docker-compose up -d --build

- `up`: This command is used to start the Docker Compose application.
- `-d`: This option runs the containers in detached mode, which means the containers will run in the background and the command prompt will return to the user.
- `--build`: This option tells Docker Compose to rebuild the Docker images before starting the containers. This is useful when you've made changes to your application's code or configuration, and you want to ensure that the latest changes are reflected in the running containers.

In summary, this command will start the Docker Compose application in detached mode and rebuild the Docker images if necessary. This is a common command used during the development and deployment of multi-container Docker applications.

