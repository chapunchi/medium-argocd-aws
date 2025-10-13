# medium-argocd-aws
Argocd pipeline with AWS test


# ArgoCD first steps

## Deployment steps
1. 
```bash
eksctl create cluster \
  --name argocd-dev \
  --region ap-southeast-1 \
  --nodes 2 \
  --nodes-min 1 \
  --nodes-max 3 \
  --node-type t3.medium \
  --managed
```

```bash
eksctl create cluster \
  --name argocd-stg \
  --region ap-southeast-1 \
  --nodes 3 \
  --nodes-min 2 \
  --nodes-max 5 \
  --node-type t3.large \
  --managed
```

```bash
eksctl create cluster \
  --name argocd-prod \
  --region ap-southeast-1 \
  --nodes 4 \
  --nodes-min 4 \
  --nodes-max 10 \
  --node-type m5.large \
  --managed
```

2. 
```bash
kubectl get nodes
```

3.
```bash
kubectl create namespace argocd
```

4.
```bash
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

5.
```bash
kubectl get pods -n argocd
```

6.
Create the manifest files,

```python
k8s-manifests/
  deployment.yaml
  service.yaml
```

7.
Push to github repo

8. 
Install argocd CLI,

```bash
brew install argocd
```

9.
```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

10.
Get the initial password,
```bash
kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}" | base64 -d; echo
```

11. 
Use the password from above command,
```bash
argocd login localhost:8080 --username admin --password <password> --insecure
```

12.
Create k8s secret key,

```bash
kubectl create secret generic repo-ssh-key \
  --from-file=sshPrivateKey=/Users/chandirapunchihewa/.ssh/argocd-key \
  -n argocd
```

13.
```bash
argocd repo add git@github.com:chapunchi/argocd-test.git \
  --ssh-private-key-path ~/.ssh/argocd-key
```

14.
```bash
argocd app create argocd \
  --repo git@github.com:chapunchi/argocd-test.git \
  --path k8s-manifests \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace default \
  --sync-policy automated
```

15.
```bash
argocd app list
```

16. 
```bash
kubectl get all -n default
```

17.
Do the change to manifest file and push to github

18.
```bash
argocd app get argocd
```

19.
```bash
kubectl get all -n default
```