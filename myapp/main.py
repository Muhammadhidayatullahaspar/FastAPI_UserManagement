from usermanagement import router as usermanagement_router
from login import router as login_router
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, OAuth2PasswordRequestForm
from jose import jwt
from sqlalchemy.orm import Session
from models import User, SessionLocal, Token
from auth import SECRET_KEY, ALGORITHM

app = FastAPI()
bearer_scheme = HTTPBearer()
app.include_router(usermanagement_router, prefix="/users", tags=["User Management"])
app.include_router(login_router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def read_root():
    return {"message": "Wellcome to user management"}
