import json
from validation.validator import validate_product

with open("data/sample_products.json") as f:
    products = json.load(f)

for p in products:
    print("\nProduct:", p)
    print(validate_product(p))