./bin/sh
docker pull batwings4724/userservice:1.0.0
docker stop userservice
docker rm userservice
docker run -d -p 4001:4001 --name userservice batwings4724/userservice:1.0.0