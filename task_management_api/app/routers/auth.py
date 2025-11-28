from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import UserLogin, Token
from ..crud.user_crud import authenticate_user
from ..auth import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    auth_user = authenticate_user(db, user.username, user.password)
    if not auth_user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_access_token({"sub": auth_user.username})

    return {"access_token": token, "token_type": "bearer"}

from ..crud.user_crud import create_user
from ..schemas import UserCreate

