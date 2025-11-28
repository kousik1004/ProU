from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi import HTTPException
from ..models import User

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def create_user(db: Session, username: str, password: str):
    existing = db.query(User).filter(User.username == username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed = pwd_context.hash(password)
    user = User(username=username, password_hash=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not user.verify_password(password):
        return None
    return user
