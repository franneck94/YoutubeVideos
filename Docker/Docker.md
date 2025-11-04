# Docker

## Docker Basics 101

- Default registry is dockerhub.io
- Install a certain version:
  - docker pull xxx:VRS
- When running a container of a certain image docker will generate a random name 
- docker logs {CONTAINER_ID}: to see logs good if ran in -d detached modes
- Port binding: nginx 80 port on container -> per default not acces. on host
  - -p flag for port binding   {HOST_PORT}:{CONTAINER_PORT}
  - only one service can run on a specific port
- docker ps -a
  - shows also stopped containers
- docker start/stop {CONTAINER_ID} or {CONTAINER_NAME}
  - to give user defined name use --name flag at docker run
- Dockerfile
  - build a docker image from it
  - Dockerfiles start from a base image (parent)
  - WORKDIR sets working dir, e.g. if files are copied to /app/
  - the last "RUN" command in a dockerfile is "CMD"
  - docker build -t {name}:{tag} {DOCKER_FILE_LOCATION}
- Docker containers communicate in an isolated docker network
  - docker network ls
  - docker network create {NAME}
  - docker run ... --network {NAME}
- Setting env variables with -e flag for docker run
- Containers have no persitence

## Docker Compose 101

- Multiple docker containers in one environment
- Compose sets up a single network for your app

yaml
services:
    service1:
        image: base_image
        ports:
            - ...
        environment:
            - ...

    service2:
        - ...


- docker compose adds as pre and suffix to the service/container names from the yaml
- controlled startup order:
  - depends_on attribute in the compose file
- docker compose down
  - will also delete the stopped containers
- docker compose stop
  - will just stop them
- Docker compose file can also refer to a dockerfile
- Using env vars from the system
  - ${ENV_VAR}
