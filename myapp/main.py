from fastapi import FastAPI
from usermanagement import router as usermanagement_router
from login import router as login_router

app = FastAPI()

app.include_router(usermanagement_router, prefix="/users", tags=["User Management"])
app.include_router(login_router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def read_root():
    return {"message": "Wellcome to user management"}
