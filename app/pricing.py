def calculate_price(
    unit_price: float,
    quantity: int,
) -> float:

    if quantity <= 0:
        raise ValueError("Quantity must be positive")

    return unit_price * quantity