# Projet Starter Azure DevOps (Python & Ubuntu)

Ce dépôt contient une structure de base prête à l'emploi pour démarrer avec **Azure DevOps** (Repos, Boards et Pipelines) sur un environnement **Python** exécuté sur un agent **Ubuntu**.

## Structure du projet

- `.azuredevops/pipelines/ci-build.yml` : Pipeline d'intégration continue exécutant `pytest` sur `ubuntu-latest`.
- `.azuredevops/pipelines/cd-deploy.yml` : Modèle de pipeline de déploiement continu.
- `.azuredevops/pull_request_template.md` : Modèle automatique pour vos Pull Requests.
- `src/app.py` : Code source de l'application Python.
- `tests/test_app.py` : Tests unitaires avec `pytest`.
- `requirements.txt` : Dépendances du projet.

## Démarrage rapide

1. Créez un nouveau projet dans **Azure DevOps**.
2. Importez ces fichiers dans **Azure Repos**.
3. Allez dans **Pipelines** > **New pipeline** > **Azure Repos Git** > **Existing Azure Pipelines YAML file** et sélectionnez `/.azuredevops/pipelines/ci-build.yml`.
