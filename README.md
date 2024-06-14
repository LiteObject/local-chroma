# Setup Chroma DB in Docker
Chroma is a open-source embedding database.

## Run the docker compose file
    docker-compose up -d

- `up`: This command is used to start the Docker Compose application.
- `-d`: This option runs the containers in detached mode, which means the containers will run in the background and the command prompt will return to the user.

In summary, this command will start the Docker Compose application in detached mode. This is a common command used during the development and deployment of multi-container Docker applications.

## Visit one of the links to verify the availability of the vectorstore
    http://localhost:8000/docs
    http://localhost:8000/api/v1/heartbeat

## Create a new collection, named 'playground', using the API
    curl -X 'POST' 'http://localhost:8000/api/v1/collections?tenant=default_tenant&database=default_database' `
     -H 'accept: application/json' `
     -H 'Content-Type: application/json' `
     -d '{ "name": "playground", "get_or_create": false}'

Alternatively, you can also write the entire command on a single line without the need for backticks:

    curl -X 'POST' 'http://localhost:8000/api/v1/collections?tenant=default_tenant&database=default_database' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{ "name": "playground", "get_or_create": false}'


## Now, let's check the result

    curl http://localhost:8000/api/v1/collections
