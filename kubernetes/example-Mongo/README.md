# MongoDB and Mongo Express Example

## Run Step
- start minikube
```sh
minikube start

# open ingress
minikube addons enable ingress
```
- apply configMap and secret
```sh
kubectl apply -f mongo-configmap.yml
kubectl apply -f mongo-express-secret.yml
kubectl apply -f mongodb-secret.yml
```

- apply deployment of MongoDB
```sh
kubectl apply -f mongodb.yml
```

- apply deployment of Mongo Express
```sh
kubectl apply -f mongo-express.yml
```

- open host file
```sh
sudo nano /etc/hosts
```

- add this line to /etc/hosts

```conf
# /etc/hosts
...
# you can get Ingress_IP from "kubectl get ingress" command
<Ingress_IP>        mongo-express-ingress.com
...
```

- go to mongo express app in `http://mongo-express-ingress.com`
- Login with username=`admin` and password=`qwer1234` (you can change it in `mongo-express-secret.yml`)
- Finish! 