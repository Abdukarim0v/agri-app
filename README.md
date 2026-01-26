# Agri App – DevOps Implementation Project

## Overview
This project demonstrates a complete DevOps implementation for a containerized
Python-based application called **Agri App**. The primary goal of this project
is to apply modern DevOps practices including CI/CD automation, GitOps-based
deployment, Kubernetes orchestration, and observability using monitoring tools.

## Technology Stack
- **Application**: Python (Flask)
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Container Registry**: Docker Hub
- **Orchestration**: Kubernetes
- **Deployment Management**: Helm
- **GitOps**: Argo CD
- **Monitoring & Metrics**: Prometheus and Grafana

## CI/CD Pipeline
The CI/CD pipeline is implemented using **GitHub Actions**.  
On every push to the `main` branch:
1. Docker image is built
2. Image is pushed to Docker Hub
3. Image tag is automatically updated in Helm values
4. Changes are committed back to the repository

.github/workflows/

## GitOps Deployment with Argo CD
Argo CD continuously monitors this repository and automatically synchronizes
Kubernetes resources using the Helm chart located in:

helm-agri-app/


The application is deployed into the **agri** namespace and maintains:
- Automated synchronization
- Self-healing
- Version tracking

## Monitoring and Observability
The project includes monitoring using:
- **Prometheus** for metrics collection
- **Grafana** for visualization

The application exposes:
- `/health` – health check endpoint
- `/metrics` – Prometheus metrics endpoint

## Repository Structure

.
├── .github/workflows # CI/CD pipelines
├── environments/dev # Environment-specific Helm values
├── helm-agri-app # Helm chart
├── Dockerfile # Docker image definition
├── app.py # Application source code
├── requirements.txt # Python dependencies
├── servicemonitor-agri.yaml # Prometheus ServiceMonitor
└── README.md


## GitHub Repository
The full source code and DevOps implementation can be found here:
https://github.com/Abdukarim0v/agri-app

## Author
Fayzulloh Abdukarimov  
DevOps Project – 2026


helm-agri-app/Workflow files are located in:

