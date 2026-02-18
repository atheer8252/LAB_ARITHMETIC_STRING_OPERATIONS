price = 2.99        # cost of one item
quantity = 3        # number of items
tax_rate = 0.075    # 7.5% tax rate in decimal form

# Calculate subtotal
subtotal = price * quantity

# Calculate tax
tax = subtotal * tax_rate

# Calculate total cost
total = subtotal + tax

# Print results formatted as currency (two decimal places)
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax:      ${tax:.2f}")
print(f"Total:    ${total:.2f}")