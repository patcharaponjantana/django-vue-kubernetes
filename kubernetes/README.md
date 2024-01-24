# 

```sh
# login to docker hub
docker login

```
- push frontend image
```sh
#
docker tag django-vue-kubernetes-frontend patcharapon1995/booking-frontend
docker push patcharapon1995/booking-frontend
```

- push backend image
```sh
#
docker tag django-vue-kubernetes-backend patcharapon1995/booking-backend
docker push patcharapon1995/booking-backend
```

- deploy all things
```sh
kubectl apply -f configmap.yml
kubectl apply -f secret.yml
kubectl apply -f database.yml
kubectl apply -f backend.yml
kubectl apply -f frontend.yml
kubectl apply -f ingress.yml
```

- check all pod are working
```sh
kubectl get pod

```

output should look like this
```sh
NAME                                   READY   STATUS    RESTARTS   AGE
backend-deployment-6657546c4b-pwsdc    1/1     Running   0          4m1s
database-deployment-689c4b4676-lvhtx   1/1     Running   0          16h
frontend-deployment-7c66f59875-924nn   1/1     Running   0          12m
```

- migrate database
```sh
kubectl exec <BACKEND_POD_NAME> -it -- bash

# example
# kubectl exec backend-deployment-6657546c4b-pwsdc -it -- bash

# in container
python manage.py migrate
```

- add host name `/etc/hosts`
```sh
<Ingress_IP>       api.mybooking.com mybooking.com

# example
192.168.49.2       api.mybooking.com mybooking.com
```

- check the result in browser
    - api.mybooking.com 
    - mybooking.com
