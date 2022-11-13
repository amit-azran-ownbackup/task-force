"""Main FastAPI app instance declaration."""

from fastapi import FastAPI
from app.db import SessionLocal

from app.api.api import api_router

app = FastAPI()
app.include_router(api_router)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Sets all CORS enabled origins
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[str(origin) for origin in config.settings.BACKEND_CORS_ORIGINS],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# Guards against HTTP Host Header attacks
# app.add_middleware(TrustedHostMiddleware, allowed_hosts=config.settings.ALLOWED_HOSTS)
