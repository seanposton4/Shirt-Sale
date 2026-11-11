import pandas as pd
from typing import List, Dict

printful_shirt_cost: float = 21.35
printful_shipping_cost: float = 9.35
tax_percent: float = 7.82
bulk_discount_percent: int = 13
required_units_for_bulk_discount: int = 25
unit_quantities: List[int] = [1, 5, 10, 20, 25, 50, 75, 100]

def percentage(percent: int) -> float:
    return percent / 100

def qualifies_for_bulk_discount(units: int) -> bool:
    return units >= 25

def calculate_cost_per_units(units: int, shirt_cost: float) -> float:
    product_cost: float = units * shirt_cost
    tax_cost: float = product_cost * percentage(tax_percent)

    total_cost: float = product_cost + tax_cost + printful_shipping_cost
    discount_cost: float = total_cost - total_cost * percentage(bulk_discount_percent)

    return total_cost if not qualifies_for_bulk_discount(units) else discount_cost

def calculate_profit_per_units(units: int, shirt_cost: float, shirt_sale_price: float) -> float:
    total_cost: float = calculate_cost_per_units(units, shirt_cost)
    total_revenue: float = units * shirt_sale_price

    return total_revenue - total_cost

def find_minimum_profitable_sale_quantity(shirt_sale_price: float, total_cost: float) -> int:
    quantity: int = 0
    while (quantity * shirt_sale_price) < total_cost:
        quantity += 1
    return quantity

def calculate_dataframe(shirt_sale_price: float):
    table: Dict[str, List[float]] = {}
    cost_quantities: List[float] = [calculate_cost_per_units(quantity, printful_shirt_cost) for quantity in unit_quantities]
    revenue_quantities: List[float] = [shirt_sale_price * quantity for quantity in unit_quantities]
    profit_quantities: List[float] = [calculate_profit_per_units(quantity, printful_shirt_cost, shirt_sale_price) for quantity in unit_quantities]
    shirt_sale_price_quantities: List[float] = [shirt_sale_price for x in range(len(unit_quantities))]
    quantity_to_profit: List[int] = [find_minimum_profitable_sale_quantity(shirt_sale_price, cost) for cost in cost_quantities]

    table['Quantity'] = unit_quantities
    table['Sale Price'] = shirt_sale_price_quantities
    table['Total Cost'] = cost_quantities
    table['Total Revenue'] = revenue_quantities
    table['Total Profits'] = profit_quantities
    table['Minimum Sales'] = quantity_to_profit

    def moneytize_me_cpn(vals: List[float]):
        return [f'${x:.2f}' for x in vals]

    money_table: Dict[str] = {k: moneytize_me_cpn(v) if isinstance(v[0], float) else v for k, v in table.items()}

    return pd.DataFrame(money_table)


frame_a = calculate_dataframe(25.00)
frame_b = calculate_dataframe(30.00)
frame_c = calculate_dataframe(35.00)

dataframe = pd.concat([frame_a, frame_b, frame_c], ignore_index=True)
print(dataframe)

x: float = 0.0
print(type(x))
print(isinstance(x, float))