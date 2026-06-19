

import csv
import os
from datetime import datetime

# ─── Predefined Stock Prices (USD) ───────────────────────────────────────────

STOCK_PRICES = {
    "AAPL":  182.50,  # Apple
    "TSLA":  248.00,  # Tesla
    "GOOGL": 175.30,  # Alphabet (Google)
    "MSFT":  415.00,  # Microsoft
    "AMZN":  190.80,  # Amazon
    "NFLX":  625.00,  # Netflix
    "META":  490.00,  # Meta
    "NVDA":  875.00,  # NVIDIA
}


def show_available_stocks():
    """Display the list of available stocks and their prices."""
    print("\n" + "=" * 45)
    print(f"  {'TICKER':<10} {'COMPANY':<20} {'PRICE (USD)':>10}")
    print("=" * 45)
    company_names = {
        "AAPL": "Apple", "TSLA": "Tesla", "GOOGL": "Alphabet",
        "MSFT": "Microsoft", "AMZN": "Amazon", "NFLX": "Netflix",
        "META": "Meta", "NVDA": "NVIDIA",
    }
    for ticker, price in STOCK_PRICES.items():
        print(f"  {ticker:<10} {company_names[ticker]:<20} ${price:>9.2f}")
    print("=" * 45)


def get_portfolio():
    """Interactively collect stock name and quantity from the user."""
    portfolio = {}
    print("\n  Enter your stock holdings.")
    print("  Type 'done' when finished.\n")

    while True:
        ticker = input("  Stock ticker (e.g., AAPL): ").strip().upper()
        if ticker == "DONE":
            break
        if ticker not in STOCK_PRICES:
            print(f"  ⚠️  '{ticker}' not found. Available: {', '.join(STOCK_PRICES)}")
            continue

        try:
            qty = int(input(f"  Quantity of {ticker}: ").strip())
            if qty <= 0:
                print("  ⚠️  Quantity must be a positive integer.")
                continue
        except ValueError:
            print("  ⚠️  Please enter a valid whole number.")
            continue

        if ticker in portfolio:
            portfolio[ticker] += qty
            print(f"  ✅ Updated {ticker}: total {portfolio[ticker]} shares.")
        else:
            portfolio[ticker] = qty
            print(f"  ✅ Added {qty} shares of {ticker}.")

    return portfolio


def display_portfolio(portfolio):
    """Print a formatted portfolio summary and return total value."""
    if not portfolio:
        print("\n  Your portfolio is empty.")
        return 0.0

    print("\n" + "=" * 60)
    print("            📊  YOUR STOCK PORTFOLIO SUMMARY")
    print("=" * 60)
    print(f"  {'TICKER':<8} {'SHARES':>8} {'PRICE':>12} {'VALUE':>14}")
    print("-" * 60)

    total = 0.0
    rows = []
    for ticker, qty in portfolio.items():
        price = STOCK_PRICES[ticker]
        value = price * qty
        total += value
        print(f"  {ticker:<8} {qty:>8} ${price:>11.2f} ${value:>13.2f}")
        rows.append((ticker, qty, price, value))

    print("-" * 60)
    print(f"  {'TOTAL INVESTMENT':>40}  ${total:>13.2f}")
    print("=" * 60)
    return total, rows


def save_to_csv(portfolio_rows, total):
    """Save the portfolio summary to a CSV file."""
    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Ticker", "Shares", "Price (USD)", "Value (USD)"])
        for row in portfolio_rows:
            writer.writerow(row)
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", f"{total:.2f}"])
    print(f"\n  💾 Portfolio saved to: {filename}")


def main():
    print("\n" + "=" * 45)
    print("   💹  STOCK PORTFOLIO TRACKER  💹")
    print("=" * 45)

    show_available_stocks()
    portfolio = get_portfolio()

    if not portfolio:
        print("\n  No stocks entered. Exiting.")
        return

    result = display_portfolio(portfolio)
    if result:
        total, rows = result

        save = input("\n  Save portfolio to CSV? (yes/no): ").strip().lower()
        if save in ("yes", "y"):
            save_to_csv(rows, total)

    print("\n  Thank you for using Stock Portfolio Tracker! 📈\n")


if __name__ == "__main__":
    main()
