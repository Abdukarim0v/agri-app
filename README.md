# Agri App – Cloud-Native DevOps Platform

This project demonstrates a complete **Cloud-Native DevOps workflow** using Kubernetes, Helm, GitHub Actions, ArgoCD, and the Prometheus/Grafana monitoring stack.

The application exposes health and metrics endpoints, is fully containerized, deployed via Helm, and continuously delivered using GitOps principles.

---

## 🧱 Architecture Overview

- **Application**: Python backend exposing `/health` and `/metrics`
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Package Manager**: Helm
- **CI**: GitHub Actions
- **CD (GitOps)**: ArgoCD
- **Monitoring**: Prometheus & Grafana
- **Logging**: Loki (optional, not required for assignment)

---

## 🔄 CI/CD Pipeline

### GitHub Actions (CI)
- Builds Docker image
- Pushes image to Docker registry
- Updates image tag for GitOps deployment

📸 **GitHub Actions – Successful Pipeline**
![GitHub Actions](screenshots/github-actions.png)

---

## 🚀 Continuous Delivery with ArgoCD

ArgoCD continuously monitors the GitHub repository and ensures the Kubernetes cluster state matches the declared Helm configuration.

📸 **ArgoCD Application – Healthy & Synced**
![ArgoCD Application](screenshots/argocd-application.png)

---

## ☸️ Kubernetes Deployment

The application and database are deployed into the `agri` namespace.

📸 **Running Pods**
![Kubernetes Pods](screenshots/kubectl-pods.png)

---

## 🗄️ Database Connectivity (PostgreSQL)

The application connects to PostgreSQL using Kubernetes **Secrets** and **ClusterIP Service**.

**Verified by:**
- Running PostgreSQL pod
- Successful DNS resolution (`postgres.agri.svc.cluster.local`)
- Application health check returns OK
- Metrics endpoint is accessible

---

## ❤️ Application Health Check

📸 **Health Endpoint**
![Health Endpoint](screenshots/health-endpoint.png)


---

## 📊 Monitoring & Observability

### Prometheus Metrics

The application exposes metrics such as:
- HTTP request count
- Request latency histogram
- Custom business metrics (harvest totals)

📸 **Prometheus Metrics Endpoint**
![Prometheus Metrics](screenshots/prometheus-metrics.png)

---

### Grafana Dashboards

Custom Grafana dashboard visualizes:
- Requests per second
- Request latency (P95 / P99)
- Application readiness & liveness
- Business metrics (harvest data)

📸 **Grafana Dashboard**
![Grafana Dashboard](screenshots/grafana-dashboard.png)

---

## 🧪 Local Access (Port Forwarding)

```bash
kubectl port-forward svc/agri-app-dev-helm-agri-app -n agri 8085:8080

Health: http://localhost:8085/health

Metrics: http://localhost:8085/metrics

🏁 Conclusion

This project demonstrates a production-style DevOps setup with:

GitOps-based delivery

Observability-first monitoring

Declarative infrastructure

Cloud-native best practices

Endpoint:

