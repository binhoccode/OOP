cover_price = 24.95
discount_rate = 0.40
copies = 60
discounted_price = cover_price * (1 - discount_rate)
total_books_cost = discounted_price * copies
shipping_cost = 3 + (0.75 * (copies - 1))
total_cost = total_books_cost + shipping_cost
print(f"Total wholesale cost for 60 copies: ${total_cost:.2f}")

