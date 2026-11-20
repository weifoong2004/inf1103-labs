from discount_strategy import (
    NoDiscount,
    PercentageDiscount,
    BulkDiscount,
    StudentDiscount
)

total = 250

print("No discount:", NoDiscount().apply(total))
print("10% discount:", PercentageDiscount(10).apply(total))
print("Bulk discount:", BulkDiscount(200, 20).apply(total))
print("Student discount:", StudentDiscount().apply(total))
