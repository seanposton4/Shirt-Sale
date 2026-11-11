import pandas as pd
from typing import List, Dict

printful_shirt_cost: float = 21.35
printful_shipping_cost: float = 9.35
tax_percent: float = 7.82
bulk_discount_percent: int = 13
required_units_for_bulk_discount: int = 25
unit_quantities: List[int] = [1, 5, 10, 20, 25, 50, 75, 100]
shirt_sale_price: float = 30

def percentage(percent: int) -> float:
    return percent / 100

def make_stars(rows: int) -> str:
    star_symbol: str = '*'
    print_rows = [star_symbol for x in range(rows)]
    return ''.join(print_rows)

def qualifies_for_bulk_discount(units: int) -> bool:
    return units >= 25

def calculate_cost_per_units(units: int, shirt_cost: float) -> float:
    product_cost: float = units * shirt_cost
    tax_cost: float = product_cost * percentage(tax_percent)

    total_cost: float = product_cost + tax_cost + printful_shipping_cost
    total_cost = round(total_cost, 2)
    discount_cost: float = total_cost - total_cost * percentage(bulk_discount_percent)
    discount_cost = round(discount_cost, 2)

    return total_cost if not qualifies_for_bulk_discount(units) else discount_cost

def calculate_profit_per_units(units: int, shirt_cost: float, shirt_sale_price: float) -> float:
    total_cost: float = calculate_cost_per_units(units, shirt_cost)
    total_revenue: float = units * shirt_sale_price

    return round(total_revenue - total_cost, 2)



table: Dict[str, List[float]] = {}
cost_quantities: List[str] = [f'${calculate_cost_per_units(quantity, printful_shirt_cost)}' for quantity in unit_quantities]
profit_quantities: List[str] = [f'${calculate_profit_per_units(quantity, printful_shirt_cost, shirt_sale_price)}' for quantity in unit_quantities]
shirt_sale_price_quantities: List[str] = [f'${shirt_sale_price}' for x in range(len(unit_quantities))]

table['Quantity'] = unit_quantities
table['Total Cost'] = cost_quantities
table['Sale Price'] = shirt_sale_price_quantities
table['Total Profits'] = profit_quantities

dataframe = pd.DataFrame(table)
print(dataframe)