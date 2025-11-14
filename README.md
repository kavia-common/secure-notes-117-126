# Secure Notes App

A web-based note-taking app with user sign up, login, and secure note CRUD using React, FastAPI, and PostgreSQL.

## Getting Started

### Backend (FastAPI)

1. `cd notes_backend`
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and set DB and JWT_SECRET variables.
4. Start the backend (port 3001):  
   `uvicorn src.api.main:app --reload --host 0.0.0.0 --port 3001`

### Database (PostgreSQL)

- Start PostgreSQL and create the database named in `POSTGRES_URL`.
- Make sure the DB connection info matches the variables in `.env`.
- Backend will auto-create tables on startup.

### Frontend (React)

- The React frontend should run on port 3000.
- Set API base URL to `http://localhost:3001` in frontend `.env`.

## API Endpoints

- `POST /auth/signup`: Register new user.
- `POST /auth/login`: Login, get JWT.
- `GET /notes`: Get logged-in user's notes (JWT required).
- `POST /notes`: Create note.
- `PUT /notes/{id}`: Update note.
- `DELETE /notes/{id}`: Delete note.

Pass JWT in the `Authorization: Bearer <token>` header.

## Environment Variables

See `.env.example` for backend, and frontend project’s `.env.example`.

## Security

- Passwords are hashed (bcrypt).
- JWT is used for login sessions.
- CORS allows requests only from frontend.
