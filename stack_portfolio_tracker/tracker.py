# Hardcoded stock prices (in INR)
stock_prices = {
    'TCS': 3600,
    'INFY': 1500,
    'RELIANCE': 2800,
    'HDFC': 1700,
    'WIPRO': 460
}

portfolio = {}
total_investment = 0

print("📈 Stock Portfolio Tracker")
print("Available stocks:", ', '.join(stock_prices.keys()))
print("Enter 'done' when you are finished.\n")

# User inputs stock names and quantity
while True:
    stock_name = input("Enter stock name: ").upper()
    if stock_name == 'DONE':
        break
    if stock_name not in stock_prices:
        print("Stock not found. Please enter a valid stock name.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    investment = stock_prices[stock_name] * quantity
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    total_investment += investment

print("\n🧾 Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    print(f"{stock}: {qty} shares × ₹{price} = ₹{qty * price}")

print(f"\nTotal Investment Value: ₹{total_investment}")

# Optionally save to file
save = input("\nDo you want to save this to a file? (yes/no): ").lower()

if save == 'yes':
    filename = input("Enter file name (with .txt or .csv): ")
    with open(filename, 'w') as file:
        file.write("Stock,Quantity,Price per Share,Total Value\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            file.write(f"{stock},{qty},{price},{qty * price}\n")
        file.write(f"\nTotal Investment: ₹{total_investment}")
    print(f"✅ Portfolio saved to {filename}")
