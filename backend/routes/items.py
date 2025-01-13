from fastapi import APIRouter

router = APIRouter()

@router.get("/api/items")
async def read_items():
    return [{"id": 1, "name": "Vinod Vukkalam"}, {"id": 2, "name": "Nevaan Skanda"}]