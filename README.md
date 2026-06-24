# Application Fullstack : Angular 20, Node.js et Java 21

<img src="./ui/ganatan-about-github.png" align="right" width="140" height="140" alt="logo ganatan">

## 🚀 Objectifs du projet
---

**👉 Looking for the English version?** : [![English](./ui/version-en.png)](./README.en.md)

---

| Composant              | Description                                                   |
|------------------------|---------------------------------------------------------------|
| **Frontend**           | Angular 20 — SPA avec Routing, SSR, PWA, SEO                  |
| **Backend Javascript**         | Node.js 22 + Express — API REST avec données mockées ou BDD   |
| **Backend TypeScript** | Node.js 22 + TypeScript — API typée avec données ou BDD       |
| **Backend Spring Boot**           | Java 21 + Spring Boot — API REST simple et moderne            |

---
---

## 🌐 Démo en ligne

🔗 [Voir la démo Angular](https://angular.ganatan.com)

<p align="center">
  <a href="https://angular.ganatan.com/">
    <img src="https://media.giphy.com/media/9BuBBLc7keCgRojp92/giphy.gif" alt="Angular 20 Example Application"/>
  </a>
</p>

---

## 📁 Structure du projet

### 🧩 Frontend

- **`frontend-angular`**  
  Application Angular 19 (Incluant Routing, Lazy loading, SSR, PWA, SEO)

### 🚀 Backends

- **`backend-javascript`**  
  API Express.js en JavaScript avec PostgreSQL, MySQL ou données mockées

- **`backend-typescript`**  
  API Express.js en TypeScript avec PostgreSQL, MySQL ou données mockées

---

## 🔧 Configuration du frontend (Angular)

Dans `frontend-angular/src/environments/environment.ts` :

```ts
useDatabase: false,
backend: 'http://localhost:3000',
```

| `useDatabase` | Mode                                  |
|---------------|---------------------------------------|
| `false`       | Données **mockées** côté frontend     |
| `true`        | Données **réelles** via le backend    |

---

## 🛠 Configuration des backends

Dans le fichier `.env` :

```env
PORT=3000
DB_CLIENT=mock # mock | pg | mysql
```

| `DB_CLIENT` | Source de données      |
|-------------|------------------------|
| `mock`      | Données simulées       |
| `pg`        | PostgreSQL             |
| `mysql`     | MySQL                  |

---

## 🔗 APIs exposées

| Ressource     | URL                                     |
|---------------|------------------------------------------|
| Continents    | [http://localhost:3000/continents](http://localhost:3000/continents) |
| Cities        | [http://localhost:3000/cities](http://localhost:3000/cities)         |
| Countries     | [http://localhost:3000/countries](http://localhost:3000/countries)   |
| Persons       | [http://localhost:3000/persons](http://localhost:3000/persons)       |
| Professions   | [http://localhost:3000/professions](http://localhost:3000/professions) |

---

## ⚙️ Démarrage rapide

### ▶️ Cloner le projet

```bash
git clone https://github.com/ganatan/angular-app.git
cd angular-app
```

### ▶️ Frontend Angular

```bash
cd frontend-angular
npm install
npm start
# http://localhost:4200
```

### ▶️ Backend JavaScript

```bash
cd backend-javascript
npm install
npm start
# http://localhost:3000
```


### ▶️ Backend TypeScript

```bash
cd backend-typescript
npm install
npm start
# http://localhost:3000
```

---


## 🐳 Déploiement avec Docker

### ▶️ Prérequis
- Docker doit être installé sur votre machine : [Installation Docker](https://docs.docker.com/get-docker/)

### ▶️ Lancer le frontend Angular via Docker

```bash
docker pull ganatan/frontend-angular
docker run -d -p 4200:4200 ganatan/frontend-angular
# http://localhost:4200
```

### ▶️ Lancer le backend Javascript via Docker

```bash
docker pull ganatan/backend-javascript
docker run -d -p 8080:8080 ganatan/backend-javascript
# http://localhost:8080
```

### ▶️ Lancer le backend Typescript via Docker

```bash
docker pull ganatan/backend-typescript
docker run -d -p 8080:8080 ganatan/backend-typescript
# http://localhost:8080
```

---

## 👤 Author

- **Danny** – [www.ganatan.com](https://www.ganatan.com)

---

## 📚 Documentation

- 🇫🇷 [Tutoriels en français](https://www.ganatan.com/tutorials)  
- 🇬🇧 [Tutorials in English](https://www.ganatan.com/en/tutorials)
