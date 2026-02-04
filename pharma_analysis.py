sales_data = [
    {"product": "PainRelief", "quantity": 120, "price": 8.50},
    {"product": "PainRelief", "quantity": 80, "price": 8.50},
    {"product": "AllergyEase", "quantity": 60, "price": 12.00},
    {"product": "AllergyEase", "quantity": 40, "price": 12.00},
    {"product": "CoughStop", "quantity": 150, "price": 6.75},
]

total_sales = {}

for sale in sales_data:
    product = sale["product"]
    sale_total = sale["quantity"] * sale["price"]
    if product not in total_sales:
        total_sales[product] = 0
    total_sales[product] += sale_total

print("Total Sales by Product:")
for product, total in total_sales.items():
    print(f"- {product}: ${total:.2f}")

print("Pharma data analysis completed successfully")

with open("pharma_report.txt", "w") as report_file:
    report_file.write("Pharma Sales Analysis Report\n")
    report_file.write("Total Sales by Product:\n")
    for product, total in total_sales.items():
        report_file.write(f"- {product}: ${total:.2f}\n")
    report_file.write("Analysis generated successfully\n")
