# Retail AI Platform

A production-ready FastAPI + React + TypeScript monorepo with Docker, PostgreSQL, and Redis. Includes minimal AI/ML scaffolding points and clean architecture for a retail SaaS.

## Tech Stack
- Backend: FastAPI, SQLAlchemy, Alembic, Redis, PostgreSQL
- Frontend: React, TypeScript, Vite, Tailwind CSS, React Query
- DevOps: Docker, docker-compose

## Quick Start

1. Copy envs from examples and adjust as needed:
```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

2. Start the stack:
```bash
docker-compose up --build
```

3. Verify:
- Backend docs: http://localhost:8000/docs
- Frontend app: http://localhost:5173

## Development Workflow
- Backend live-reloads via `uvicorn --reload` in the container (mounted volume)
- Frontend runs Vite dev server in its container with hot reload
- Use `requirements-dev.txt` for tooling (pytest, mypy, flake8, black)

## Project Layout
See `docs/SETUP.md` for full details.
