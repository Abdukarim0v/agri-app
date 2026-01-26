# Agri App – DevOps Implementation Project

## Overview
This project demonstrates a complete DevOps implementation for a containerized
Python-based application called **Agri App**. The project applies modern DevOps
practices including CI/CD automation, GitOps-based deployment, Kubernetes
orchestration, and observability.

## Technology Stack
- Application: Python (Flask)
- Containerization: Docker
- CI/CD: GitHub Actions
- Container Registry: Docker Hub
- Orchestration: Kubernetes
- Deployment Management: Helm
- GitOps: Argo CD
- Monitoring & Metrics: Prometheus and Grafana

## CI/CD Pipeline
A GitHub Actions pipeline is triggered on every push to the main branch.
The pipeline builds the Docker image, pushes it to Docker Hub, and automatically
updates the image tag inside Helm values for GitOps deployment.

Workflow files are located in:
.github/workflows/

## GitOps Deployment
The application is deployed using Helm and managed by Argo CD.
Argo CD continuously monitors the repository and ensures:
- Automated synchronization
- Self-healing
- Desired state enforcement

Helm chart location:
helm-agri-app/

## Monitoring and Observability
Monitoring is implemented using Prometheus and Grafana.
The application exposes the following endpoints:
- /health – application health check
- /metrics – Prometheus metrics endpoint

## GitHub Repository
Full source code and DevOps implementation:
https://github.com/Abdukarim0v/agri-app

## Author
Fayzulloh Abdukarimov  
DevOps Assignment – 2026
