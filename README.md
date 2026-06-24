# Angular 22 Fullstack Starter

Angular 22 starter application with Node.js and Spring Boot backends.

---

## Stack

| Project | Technology |
|----------|------------|
| frontend-angular | Angular 22 |
| backend-node | Node.js + TypeScript |
| backend-springboot | Java + Spring Boot    |

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

## Quick Start

```bash
git clone https://github.com/ganatan/angular-node-java.git

cd frontend-angular

npm install

npm start
```

Open:

```text
http://localhost:4200
```

---

## Tutorial

Step-by-step tutorials are available on Ganatan:

🇫🇷 https://www.ganatan.com/tutorials

🇬🇧 https://www.ganatan.com/en/tutorials

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

## Frontend Commands

### Installation

```bash
npm install
npm outdated
```

### Development

```bash
npm start
```

Open:

```text
http://localhost:4200
```

### Production

```bash
npm run build
```

### Linter

```bash
npm run lint
```

### Tests

```bash
npm run test
```

### Coverage

```bash
npm run coverage
```

---

## Backend Node

### Installation

```bash
cd backend-node

npm install
```

### Development

```bash
npm start
```

Open:

```text
http://localhost:3000
```

### Production

```bash
npm run build
```

---

## Backend Spring Boot

### Development

```bash
cd backend-springboot

mvn spring-boot:run
```

Open:

```text
http://localhost:8080
```

### Build

```bash
mvn clean package
```

---

## Author

Danny

🌐 https://www.ganatan.com

---

