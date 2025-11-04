# Setup Guide

## Prerequisites
- Python 3.11+
- Node.js 18+
- Docker and docker-compose

## Environment Variables
Copy `.env.example` files and adjust them:
```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

## Run with Docker
```bash
docker-compose up --build
```

- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Frontend: http://localhost:5173
- Postgres: localhost:5432 (user/pass `postgres`)
- Redis: localhost:6379

## Troubleshooting
- If ports are in use, stop local services or change ports
- If Python deps fail: ensure internet access and retry `docker-compose up --build`
- Database connection issues: confirm `DATABASE_URL` and container health
- CORS: update `BACKEND_CORS_ORIGINS` in `backend/.env`
