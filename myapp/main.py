from usermanagement import router as usermanagement_router
from login import router as login_router
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, OAuth2PasswordRequestForm
from jose import jwt
from sqlalchemy.orm import Session
from models import User, SessionLocal, Token
from auth import SECRET_KEY, ALGORITHM
from fastapi.responses import HTMLResponse

app = FastAPI()
bearer_scheme = HTTPBearer()
app.include_router(usermanagement_router, prefix="/users", tags=["User Management"])
app.include_router(login_router, prefix="/auth", tags=["Authentication"])

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>User Management API</title>
        </head>
        <body>
            <h2>Welcome to the User Management API</h2>
            <p>This API allows you to manage users within the system. Use the link below to access the API documentation and interact with the API's endpoints.</p>
            <a href="/docs">Go to Swagger UI</a>
            <br><br>
            <p>Access this code on my GitHub, here's the link:</p>
            <a href="https://github.com/Muhammadhidayatullahaspar/FastAPI_UserManagement">GitHub Repository</a>
        </body>
    </html>
    """
