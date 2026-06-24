# Angular 20 Fullstack Starter

Angular 20 starter application with multiple backend implementations.

**👉 Version française:** [Français](./README.md)

---

## Stack

| Project | Technology |
|----------|------------|
| frontend-angular | Angular 20 |
| backend-javascript | Node.js + Express |
| backend-typescript | Node.js + TypeScript |
| backend-springboot | Java + Spring Boot |

---

## Architecture

```text
frontend-angular
        |
        +-- backend-javascript
        |
        +-- backend-typescript
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
backend-javascript/
backend-typescript/
backend-springboot/
ui/
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
| false | Use frontend mock data |
| true | Use backend API |

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

### Clone the repository

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

### JavaScript Backend

```bash
cd backend-javascript
npm install
npm start
```

http://localhost:3000

### TypeScript Backend

```bash
cd backend-typescript
npm install
npm start
```

http://localhost:3000

### Spring Boot Backend

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

### JavaScript Backend

```bash
docker pull ganatan/backend-javascript
docker run -d -p 8080:8080 ganatan/backend-javascript
```

### TypeScript Backend

```bash
docker pull ganatan/backend-typescript
docker run -d -p 8080:8080 ganatan/backend-typescript
```

---

## Author

Danny

🌐 https://www.ganatan.com

---

## Documentation

🇫🇷 https://www.ganatan.com/tutorials

🇬🇧 https://www.ganatan.com/en/tutorials