# Taller K8S — Microservicio con Docker, Kubernetes, Helm, ArgoCD y GitHub Actions

Universidad de La Sabana — Maestría en Ingeniería de Software  
Arquitectura de Software

---

## Descripción

Este proyecto implementa un microservicio básico desplegado con una arquitectura moderna de contenedores y GitOps. El microservicio fue construido con FastAPI (Python) y desplegado usando Docker, Kubernetes, Helm y ArgoCD, con automatización CI/CD mediante GitHub Actions.

---

## Tecnologías utilizadas

| Tecnología | Versión | Uso |
|---|---|---|
| Python / FastAPI | 3.11 | Microservicio REST |
| Docker | 29.4.3 | Contenedorización |
| Kubernetes (Minikube) | v1.35.1 | Orquestación de contenedores |
| Helm | v4.2.1 | Gestión de paquetes K8S |
| ArgoCD | v3.4.4 | Despliegue GitOps |
| GitHub Actions | — | Pipeline CI/CD |

---

## Estructura del proyecto

```
taller-k8s/
├── app/
│   ├── main.py                  # Código fuente del microservicio
│   └── requirements.txt         # Dependencias Python
├── mi-microservicio-chart/      # Helm chart
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
│       ├── deployment.yaml
│       └── service.yaml
├── .github/
│   └── workflows/
│       └── ci-cd.yaml           # Pipeline GitHub Actions
└── Dockerfile                   # Imagen Docker del microservicio
```

---

## Microservicio

El microservicio expone dos endpoints:

| Endpoint | Método | Respuesta |
|---|---|---|
| `/` | GET | `{"message": "Hola desde mi microservicio!", "status": "ok"}` |
| `/health` | GET | `{"status": "healthy"}` |

---

## Pasos para ejecutar localmente

### 1. Clonar el repositorio

```bash
git clone https://github.com/JHBOGameDev/taller-k8s.git
cd taller-k8s
```

### 2. Construir y correr con Docker

```bash
docker build -t mi-microservicio:v1 .
docker run -d -p 8000:8000 --name mi-microservicio mi-microservicio:v1
```

Acceder en: `http://localhost:8000`

### 3. Desplegar en Kubernetes con Helm

```bash
minikube start
helm install mi-microservicio ./mi-microservicio-chart
kubectl get pods
minikube service mi-microservicio --url
```

### 4. Acceder a ArgoCD

```bash
kubectl port-forward svc/argocd-server -n argocd 8081:443
```

Acceder en: `https://localhost:8081`  
Usuario: `admin`

---

## Pipeline CI/CD

El pipeline de GitHub Actions se activa automáticamente con cada `push` a la rama `main` y ejecuta los siguientes pasos:

1. Checkout del código
2. Login a Docker Hub
3. Build de la imagen Docker
4. Push de la imagen a Docker Hub con el tag del commit (`github.sha`)

El pipeline está definido en `.github/workflows/ci-cd.yaml`.

---

## ArgoCD — GitOps

ArgoCD monitorea el repositorio de GitHub y sincroniza automáticamente cualquier cambio en el Helm chart con el clúster de Kubernetes.

- **Repositorio:** https://github.com/JHBOGameDev/taller-k8s
- **Path:** `mi-microservicio-chart`
- **Rama:** `main`
- **Namespace:** `default`
- **Sync Policy:** Automático

---

## Imagen en Docker Hub

```
josebao/mi-microservicio:v1
```

👉 https://hub.docker.com/r/josebao/mi-microservicio

---

## Entregables

- Código fuente: https://github.com/JHBOGameDev/taller-k8s
- Video de demostración: [enlace al video]