# Ferry Booking App
This is the example code for ferry booking

## Technologies
- Vue 3 (with Vite)
- Django 4.12
- PostgreSQL

## Prerequisite
- docker compose v2   
if your machine doesn't have docker compose v2 yet, you can install from this script

```sh
# install docker 
sudo apt update
sudo apt install docker.io

# install docker compose v2. see more https://docs.docker.com/compose/install/linux/
DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
mkdir -p $DOCKER_CONFIG/cli-plugins
curl -SL https://github.com/docker/compose/releases/download/v2.20.3/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose

chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
```

check the installation
```sh
docker compose version
# Docker Compose version v2.20.3
```

## Deploy all services

### With Docker Compose
```sh
docker compose up
```

frontend: http://localhost:3000  
backend: http://localhost:8000

### With Kubernetes
To Do

## Screenshot

### Frontend
![02_frontend_home](/_docs/02_frontend_home.png "02_frontend_home")
![03_frontend_search](/_docs/03_frontend_search.png "03_frontend_search")
![04_frontend_itinerary](/_docs/04_frontend_itinerary.png "04_frontend_itinerary")
![05_frontend_passenger](/_docs/05_frontend_passenger.png "05_frontend_passenger")
![06_frontend_payment](/_docs/06_frontend_payment.png "06_frontend_payment")
![07_frontend_bookingsuccess](/_docs/07_frontend_bookingsuccess.png "07_frontend_bookingsuccess")

### Backend
![08_backend_api](/_docs/08_backend_api.png "08_backend_api")
![09_backend_api_response](/_docs/09_backend_api_response.png "09_backend_api_response")