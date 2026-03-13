# Docker Compose - Architecture Microservices (Frontend + Backend)

## 📝 Présentation du projet

Ce projet est une infrastructure web complète utilisant **Docker Compose** avec deux services distincts qui communiquent ensemble :
- **Backend** (Python/Flask) : Une API qui traite les données
- **Frontend** (Nginx) : Une interface web qui affiche les données

## 🏗️ Architecture du projet

```
┌─────────────────────────────────────────────────────────────┐
│                     DOCKER COMPOSE                          │
│                                                             │
│   ┌─────────────────────┐     ┌─────────────────────┐     │
│   │    BACKEND          │     │    FRONTEND         │     │
│   │  (Python/Flask)     │     │    (Nginx)          │     │
│   │                     │     │                     │     │
│   │  Port 5000          │◄────┤    Port 80          │     │
│   │  (interne)          │     │    (interne)        │     │
│   └─────────┬───────────┘     └─────────┬───────────┘     │
│             │                           │                  │
│   Exposé   │                           │  Exposé         │
│   sur :5000│                           │  sur :8080       │
└─────────────┴───────────────────────────┴──────────────────┘
```

### Service Backend (Python/Flask)
- **Image** : Custom (construite depuis `backend/Dockerfile`)
- **Port exposé** : `5000`
- **Route API** : `/api/message`
- **Rôle** : Retourne un message JSON, gère le CORS

### Service Frontend (Nginx)
- **Image** : Custom (construite depuis `frontend/Dockerfile`)
- **Port exposé** : `8080` (mappé vers le port 80 du conteneur)
- **Rôle** : Sert une page HTML avec JavaScript qui fetch les données du backend

### Communication
- Le frontend utilise `fetch()` pour appeler le backend via `http://localhost:5000/api/message`
- Le CORS est activé sur le backend pour permettre les requêtes cross-origin

## 🚀 Commandes minimales pour lancer le projet

### Prérequis
- Docker installé sur le VPS
- Docker Compose installé

### Lancer l'infrastructure
```bash
docker-compose up --build -d
```


### Arrêter l'infrastructure
```bash
docker-compose down
```


## 💡 Notes techniques importantes

### CORS (Cross-Origin Resource Sharing)
- Sans l'extension `flask-cors` dans le backend, le navigateur bloquerait les requêtes du frontend
- Le frontend est sur `localhost:8080` et le backend sur `localhost:5000` - ce sont des origines différentes

### Ports utilisés
| Service | Port interne | Port exposé |
|---------|--------------|--------------|
| Backend (Flask) | 5000 | 5000 |
| Frontend (Nginx) | 80 | 8080 |

### Réseau Docker
- Un réseau bridge nommé `le_reseau` permet la communication entre les conteneurs
- Le frontend peut accéder au backend via le nom du service `http://backend:5000` (depuis un autre conteneur)

## 🎁 Features en bonus

### 1. Redémarrage automatique
- Les conteneurs redémarrent automatiquement avec `restart: unless-stopped`
- Utile si le VPS reboot

### 2. Mode production
- Variables d'environnement configurées pour désactiver le debug Flask

### 3. Configuration Nginx sécurisée
- Headers de sécurité ajoutés (X-Frame-Options, X-Content-Type-Options, X-XSS-Protection)
- Support SPA avec try_files (pour les applications React/Vue)

### 4. Dépendance explicite
- Le frontend dépend du backend (`depends_on`)
- Docker-compose démarre le backend avant le frontend

J'ai développé mon TP et ai généré le readme par IA pour la présentation.