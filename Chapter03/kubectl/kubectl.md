# kubectl
```
kubectl describe
kubectl get 
kubectl delete
kubectl logs

```
# CRDS
```
kubectl get crds
```

# provider
```
kubectl get providers
kubectl get providerconfig
kubectl get providerrevisions  
```
# configuration  
``` 
kubectl get configurationrevisions             
kubectl get configurations
```
# crossplane
```
kubectl get crossplane
kubectl get managed
```
# composition
```
# kubectl get composite
kubectl get compositeresourcedefinitions 
kubectl get compositions
kubectl get composition
kubectl get compositionrevisions 
# kubectl get claim
```

# others
```
kubectl get pkg
kubectl get locks
kubectl get controllerconfigs   
kubectl get storeconfigs 
```

# troubleshooting
```
kubectl get events
```

## crossplane:
```
kubectl -n crossplane-system logs -lapp=crossplane
kubectl -n crossplane-system  get pod
kubectl -n crossplane-system logs <name-of-provider-pod>
```


## upbound:
```
kubectl -n upbound-system  logs -lapp=crossplane
kubectl -n upbound-system  get pod 
kubectl -n  upbound-system logs upbound-provider-aws-c49e1af5e48d-789bcd89c7-qr8b4 -f
```

## Clean
```
kubectl patch <resource-type> <resource-name> -p '{"metadata":{"finalizers": []}}' --type=merge
kubectl patch cloudsqlinstance my-db -p '{"metadata":{"finalizers": []}}' --type=merge
```

```
kubectl patch providerconfig.gcp.crossplane.io default -p '{"metadata":{"finalizers": []}}' --type=merge

```