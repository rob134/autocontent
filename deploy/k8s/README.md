# Kubernetes (baseline)

Apply after pushing images:

```bash
kubectl apply -f deploy/k8s/
```

Contains baseline Deployments/Services for:
- backend (python ai)
- orchestrator-java
- kafka (single node dev profile)
