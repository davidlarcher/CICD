from fastapi import FastAPI

from app.pricing import calculate_price

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/quotes")
def create_quote(
    unit_price: float,
    quantity: int,
):
    total = calculate_price(unit_price, quantity)

    return {
        "unit_price": unit_price,
        "quantity": quantity,
        "total": total,
    }