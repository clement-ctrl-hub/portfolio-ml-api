# 🚀 API de Machine Learning déployée sur AWS

Ce projet présente le déploiement complet d'une API de Machine Learning en production sur AWS.
<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="50" alt="Python"/>&nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width="50" alt="FastAPI"/>&nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="50" alt="Docker"/>&nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="50" alt="GitHub"/>&nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/githubactions/githubactions-original.svg" width="50" alt="GitHub Actions"/>&nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" width="60" alt="AWS"/>
</p>

L'application est développée avec **FastAPI**, conteneurisée avec **Docker** et déployée automatiquement sur une instance **Amazon EC2** grâce à un pipeline **CI/CD GitHub Actions**. Les images Docker sont stockées dans **Amazon ECR** et l'API est exposée via un **Application Load Balancer**.

## Fonctionnalités

- API REST développée avec FastAPI
- Prédiction à partir d'un modèle de Machine Learning
- Documentation interactive avec Swagger (`/docs`)
- Vérification de l'état de l'API (`/health`)
- Déploiement automatique après chaque `git push`
- Hébergement sur AWS

## Technologies utilisées

- Python
- FastAPI
- Scikit-learn
- Docker
- GitHub Actions
- Amazon EC2
- Amazon ECR
- AWS Systems Manager (SSM)
- Application Load Balancer (ALB)

## Pipeline CI/CD

À chaque mise à jour du dépôt GitHub :

1. Les tests sont exécutés.
2. Une nouvelle image Docker est construite.
3. L'image est envoyée vers Amazon ECR.
4. L'instance EC2 récupère automatiquement la nouvelle image.
5. Le conteneur est redémarré avec la dernière version de l'application.

## Endpoints

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Vérifie que l'API est opérationnelle |
| GET | `/health` | Vérifie l'état du modèle |
| POST | `/predict` | Retourne une prédiction |
| GET | `/docs` | Documentation Swagger |

## Auteur

**Clément Amegadjaka**

Projet réalisé dans le cadre de mon portfolio afin de démontrer mes compétences en **Machine Learning**, **Docker**, **AWS** et **CI/CD**.