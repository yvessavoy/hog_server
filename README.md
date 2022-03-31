# HOG Server
## Setup and run Grafana and the HOG-Server with docker
1. Create 2 volumes for persisting grafana and hog-data:
```docker
docker volume create grafana-storage
docker volume create hog-storage
````
2. Run the container with exposed ports and both volumes:
```docker
docker run -p 3000:3000 -p 3001:3001 -v grafana-storage:/var/lib/grafana -v hog-storage:/app hog_server
```