from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import User, Token, SessionLocal
from auth import create_access_token, verify_password, get_password_hash, get_current_user
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

class UserRegister(BaseModel):
    username: str
    password: str
    
class UserLogin(BaseModel):
    username: str
    password: str

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/token")
def login(form_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token, expiration = create_access_token(data={"sub": user.username})
    token_record = Token(access_token=access_token, user_id=user.id, expiration_date=expiration)
    db.add(token_record)
    db.commit()
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/logout")
def logout(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_token = db.query(Token).filter(Token.user_id == current_user.id).first()
    if db_token:
        db.delete(db_token)
        db.commit()
        return {"message": "User logged out successfully."}
    else:
        raise HTTPException(status_code=404, detail="Token not found")

@router.post("/register")
def register_user(user_data: UserRegister, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user_data.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user_data.password)
    new_user = User(username=user_data.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User successfully registered", "username": new_user.username}