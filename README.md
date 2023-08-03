# Pezesha

![Pezesha](./pezesha.png)

# Auth

![auth](./token.png)

# Run Django with Docker Compose

Run services in the background:
`docker-compose up -d`

Run services in the foreground:
`docker-compose up --build`

Inspect volume:
`docker volume ls`
and
`docker volume inspect <volume name>`

Prune unused volumes:
`docker volume prune`

View networks:
`docker network ls`

Bring services down:
`docker-compose down`

Open a bash session in a running container:
`docker exec -it <container ID> /bin/bash`