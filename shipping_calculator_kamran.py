# Express Shipping Rate Calculator
# Developer: Daniel Chen
# Date: March 2024

# Show program introduction
print("Welcome to Package Express. Please follow the instructions below.")

# Get package weight
weight_value = float(input("Please enter the package weight:\n"))

# Validate weight limit
if weight_value > 50:
    print("Package too heavy to be shipped via Package Express. Have a good day.")
    exit()

# Get package dimensions
dim_w = float(input("Please enter the package width:\n"))
dim_h = float(input("Please enter the package height:\n"))
dim_l = float(input("Please enter the package length:\n"))

# Calculate total dimensions
total_dims = dim_w + dim_h + dim_l

# Validate size limit
if total_dims > 50:
    print("Package too big to be shipped via Package Express.")
    exit()

# Calculate shipping cost
# Cost = (width * height * length * weight) / 100
final_cost = (dim_w * dim_h * dim_l * weight_value) / 100

# Show shipping cost
print(f"Your estimated total for shipping this package is: ${final_cost:.2f}")
print("Thank you!") 