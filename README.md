# Angular 22 Fullstack Starter

Angular 22 starter application with multiple backend implementations.

---

## Stack

| Project | Technology |
|----------|------------|
| frontend-angular | Angular 22 |
| backend-node       | Node.js + TypeScript |
| backend-springboot | Java + Spring Boot |

---

## Architecture

```text
frontend-angular
        |
        +-- backend-node
        |
        +-- backend-springboot
```

---

## Demo

🔗 https://angular.ganatan.com

<p align="center">
  <a href="https://angular.ganatan.com">
    <img src="https://media.giphy.com/media/9BuBBLc7keCgRojp92/giphy.gif" alt="Angular Demo">
  </a>
</p>

---

## Project Structure

```text
frontend-angular/
backend-node/
backend-springboot/
```

---

## Frontend Configuration

File:

```text
frontend-angular/src/environments/environment.ts
```

Example:

```ts
useDatabase: false,
backend: 'http://localhost:3000',
```

| Value | Description |
|---------|-------------|
| false | Frontend mock data |
| true | Backend API |

---

## Backend Configuration

File:

```text
.env
```

Example:

```env
PORT=3000
DB_CLIENT=mock
```

| Value | Description |
|---------|-------------|
| mock | Mock data |
| pg | PostgreSQL |
| mysql | MySQL |

---

## Available APIs

```text
GET /continents
GET /countries
GET /cities
GET /persons
GET /professions
```

---

## Quick Start

### Clone

```bash
git clone https://github.com/ganatan/angular-node-java.git
cd angular-node-java
```

### Frontend

```bash
cd frontend-angular
npm install
npm start
```

http://localhost:4200


### Backend Node

```bash
cd backend-node
npm install
npm start
```

http://localhost:3000

### Backend Spring Boot

```bash
cd backend-springboot
mvn spring-boot:run
```

http://localhost:8080

---

## Docker

### Frontend

```bash
docker pull ganatan/frontend-angular
docker run -d -p 4200:4200 ganatan/frontend-angular
```

### Backend Node

```bash
docker pull ganatan/backend-node
docker run -d -p 8080:8080 ganatan/backend-node
```

---

## Author

Danny 

🌐 https://www.ganatan.com

---

## Documentation

🇫🇷 https://www.ganatan.com/tutorials

🇬🇧 https://www.ganatan.com/en/tutorials