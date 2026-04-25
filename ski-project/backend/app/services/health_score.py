from pydantic import BaseModel

from app.models.product import Product


class HealthScore(BaseModel):
    score: int
    label: str
    color: str
    reasons: list[str]


def calculate_health_score(product: Product) -> HealthScore:
    nutrition = product.nutrition
    score = 100
    reasons: list[str] = []

    if nutrition.sugars is not None:
        if nutrition.sugars > 12:
            score -= 25
            reasons.append("High sugar content")
        elif nutrition.sugars < 5:
            reasons.append("Low sugar content")

    if nutrition.sodium is not None:
        sodium_mg = nutrition.sodium * 1000
        if sodium_mg > 600:
            score -= 20
            reasons.append("High sodium content")
        elif sodium_mg < 120:
            reasons.append("Low sodium content")

    if nutrition.saturated_fat is not None and nutrition.saturated_fat > 5:
        score -= 15
        reasons.append("High saturated fat")

    if product.nova_group is not None and product.nova_group >= 4:
        score -= 20
        reasons.append("Ultra-processed food")

    if nutrition.fiber is not None and nutrition.fiber >= 3:
        score += 5
        reasons.append("Good fiber content")

    score = max(0, min(100, score))

    if score >= 75:
        label = "Healthy"
        color = "green"
    elif score >= 50:
        label = "Moderate"
        color = "yellow"
    else:
        label = "Needs Caution"
        color = "red"

    if not reasons:
        reasons.append("Limited nutrition data available")

    return HealthScore(score=score, label=label, color=color, reasons=reasons)
