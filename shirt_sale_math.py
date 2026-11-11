import pandas as pd

shirt_cost: float = 21.35
shipping_cost: float = 7.15
tax_percent: float = 7.82
bulk_discount_percent: int = 13
required_units_for_bulk_discount: int = 25
units: int = 25
bulk_discount_qualifies: bool = units >= required_units_for_bulk_discount

def percentage(percent: str):
    return percent / 100

def make_stars(rows: int):
    star_symbol: str = '*'
    print_rows = [star_symbol for x in range(rows)]
    return ''.join(print_rows)

pd.