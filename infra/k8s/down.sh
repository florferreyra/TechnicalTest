#!/bin/bash

# Eliminar el ingress.yaml
echo "Eliminando ingress.yaml..."
kubectl delete -f ingress.yaml

# Eliminar los Helms de app-cargo y app-saludo
echo "Eliminando Helm de app-cargo..."
kubectl delete -f app-cargo/helms/charts/helm.yaml

echo "Eliminando Helm de app-saludo..."
kubectl delete -f app-saludo/helms/charts/helm.yaml

echo "Eliminación completada."
