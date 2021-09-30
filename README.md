# random-codname

## build the docker image
```
docker build . -t random-codname
```

## tag and push image to docker registry
```
docker tag random-codname gfnord/random-codname:latest
docker push gfnord/random-codname:latest
```

## deploy container on k8s
```
kubectl apply -f k8s-deploy-random-codname.yaml
```
