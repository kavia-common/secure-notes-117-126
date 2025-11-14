from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import create_db_and_tables
from app.routers import auth, notes

app = FastAPI(
    title="Secure Notes App API",
    description="API backend for a secure notes web application supporting authentication and CRUD operations for notes.",
    version="1.0.0",
    openapi_tags=[
        {"name": "Auth", "description": "Authentication endpoints"},
        {"name": "Notes", "description": "CRUD for user notes"},
    ],
)

# CORS config - restrict to frontend (localhost:3000)
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup():
    """Initialize database on startup."""
    create_db_and_tables()

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(notes.router, prefix="/notes", tags=["Notes"])

# PUBLIC_INTERFACE
@app.get("/", tags=["Health"])
def health_check():
    """Health check route."""
    return {"message": "Healthy"}
