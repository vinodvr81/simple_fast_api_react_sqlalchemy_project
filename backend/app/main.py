from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import items, users

my_app = FastAPI()

# CORS configuration
my_app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
my_app.include_router(items.router)
my_app.include_router(users.router)

@my_app.get("/api/health")
async def health_check():
    return {"status": "ok"}