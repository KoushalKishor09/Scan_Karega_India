from fastapi import APIRouter

from app.models.product import NutritionFacts, Product


router = APIRouter()


@router.get("/")
def list_products() -> list[Product]:
    return [
        Product(
            barcode="demo-001",
            name="Demo Muesli",
            brand="SKI",
            ingredients="Oats, nuts, seeds, dried fruit",
            nutrition=NutritionFacts(
                energy_kcal=372,
                fat=8.4,
                saturated_fat=1.2,
                sugars=7.1,
                sodium=0.08,
                fiber=8.6,
                proteins=10.2,
            ),
            nutriscore="b",
            nova_group=3,
        )
    ]
