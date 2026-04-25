from pydantic import BaseModel


class NutritionFacts(BaseModel):
    energy_kcal: float | None = None
    fat: float | None = None
    saturated_fat: float | None = None
    sugars: float | None = None
    sodium: float | None = None
    fiber: float | None = None
    proteins: float | None = None


class Product(BaseModel):
    barcode: str
    name: str
    brand: str | None = None
    ingredients: str | None = None
    nutriscore: str | None = None
    nova_group: int | None = None
    nutrition: NutritionFacts = NutritionFacts()
