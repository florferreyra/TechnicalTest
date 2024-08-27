#!/bin/bash

# Levantar los Helms de app-cargo y app-saludo
echo "Levantando Helm de app-cargo..."
kubectl apply -f app-cargo/helms/charts/helm.yaml

echo "Levantando Helm de app-saludo..."
kubectl apply -f app-saludo/helms/charts/helm.yaml

# Esperar 20 segundos
echo "Esperando 20 segundos para que los deployments se estabilicen..."
sleep 20

# Levantar el ingress.yaml
echo "Levantando ingress.yaml..."
kubectl apply -f ingress.yaml

echo "Despliegue completado."
