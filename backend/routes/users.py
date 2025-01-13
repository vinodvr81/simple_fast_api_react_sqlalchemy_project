from fastapi import APIRouter

router = APIRouter()

@router.get("/api/users")
async def read_users():
    return [{"id": 1, "username": "Vinod Vukkalam"}, {"id": 2, "username": "Nevaan Skanda"}]