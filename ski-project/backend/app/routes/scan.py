from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def scan_status() -> dict[str, str]:
    return {"status": "ready", "message": "Barcode scan endpoint scaffolded"}
