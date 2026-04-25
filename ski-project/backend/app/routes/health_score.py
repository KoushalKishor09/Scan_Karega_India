from fastapi import APIRouter

from app.models.product import Product
from app.services.health_score import HealthScore, calculate_health_score


router = APIRouter()


@router.post("/")
def score_product(product: Product) -> HealthScore:
    return calculate_health_score(product)
