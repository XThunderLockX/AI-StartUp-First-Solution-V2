# API Overview

Base path: `/api/v1`

## Authentication
- JWT-based authentication via `Authorization: Bearer <token>` header
- Token issuance endpoint (placeholder): `POST /api/v1/auth/login`

## Health
- `GET /api/v1/health` returns basic service status

## Hello
- `GET /api/v1/hello` returns a greeting for frontend connectivity tests
