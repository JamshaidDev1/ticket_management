# Customer Support Assistant API

## Overview
This is a production-level FastAPI backend for a Customer Support Assistant system. It includes authentication, ticket management, and AI-powered responses.

## Features
- JWT-based authentication
- Role-based permissions (user, admin)
- Ticket management system
- AI response generation via SSE
- PostgreSQL database
- Dockerized deployment

## Setup

### Prerequisites
- Docker and Docker Compose
- Python 3.9+

### Installation
1. Clone the repository
2. Copy `.env.example` to `.env` and fill in the values
3. Run `docker-compose up --build`

### Running Tests
```bash
docker-compose run web pytest
```

### Formatting and Linting
```bash
docker-compose run web black .
docker-compose run web isort .
docker-compose run web mypy .
```

## Architecture
The application follows a service-oriented architecture with clear separation of concerns:
- API Layer: Handles HTTP requests and responses
- Service Layer: Contains business logic
- Repository Layer: Manages database operations

## Design Patterns
### Factory Pattern
Used in the repository layer to create database session instances, allowing for easier testing and dependency injection.

## Challenges
- Implementing SSE for AI responses required careful handling of streaming responses
- Role-based permissions needed to be integrated with JWT authentication
- Database migrations had to be carefully managed with Alembic

## Improvements
- Add rate limiting for API endpoints
- Implement caching for frequently accessed data
- Add more comprehensive logging
- Implement background tasks for long-running operations