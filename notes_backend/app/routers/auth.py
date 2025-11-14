from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, models, auth

router = APIRouter()

# PUBLIC_INTERFACE
@router.post("/signup", response_model=schemas.TokenResponse, summary="User signup", description="Register a new user and receive a JWT token.")
def signup(user: schemas.UserSignup, db: Session = Depends(auth.get_db)):
    # Check if username already exists
    existing = db.query(models.User).filter(models.User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered.")
    hashed_pw = auth.get_password_hash(user.password)
    new_user = models.User(username=user.username, password_hash=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    access_token = auth.create_access_token(data={"sub": user.username})
    return schemas.TokenResponse(access_token=access_token)

# PUBLIC_INTERFACE
@router.post("/login", response_model=schemas.TokenResponse, summary="User login", description="Authenticate with username and password, receive JWT token.")
def login(user: schemas.UserLogin, db: Session = Depends(auth.get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or not auth.verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password.")
    access_token = auth.create_access_token(data={"sub": user.username})
    return schemas.TokenResponse(access_token=access_token)
