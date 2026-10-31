"""
=====================================================
 Project      : Stock Portfolio Tracker
 Internship   : CodeAlpha - Python Programming Internship
 Task         : Task 2 - Stock Portfolio Tracker
 Description  : A beginner-friendly command-line program
                that lets a user build a stock portfolio
                using fixed stock prices, calculates the
                total investment value, and saves the
                results to a text/CSV file.
=====================================================
"""

# We only use Python's built-in 'csv' module for the optional
# CSV export feature. Everything else is pure Python.
import csv


# ---------------------------------------------------
# Hardcoded dictionary of available stocks and prices.
# Key   -> Stock symbol (string)
# Value -> Price per share in rupees/dollars (number)
# ---------------------------------------------------
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}


# ---------------------------------------------------
# Function 1: display_available_stocks()
# Purpose: Show the user which stocks they can invest in,
#          along with their fixed price per share.
# ---------------------------------------------------
def display_available_stocks():
    print("\n--- Available Stocks ---")
    print(f"{'Symbol':<10}{'Price per Share':>18}")
    print("-" * 28)

    # Loop through the dictionary to print each stock and its price.
    for symbol, price in stock_prices.items():
        print(f"{symbol:<10}{price:>18}")

    print("-" * 28)


# ---------------------------------------------------
# Function 2: get_stock_input()
# Purpose: Ask the user how many stocks they want to enter,
#          then collect the stock name and quantity for each,
#          validating the input using try-except and if-else.
# Returns: A dictionary like {"AAPL": 10, "TSLA": 5}
# ---------------------------------------------------
def get_stock_input():
    portfolio = {}  # Will store {stock_symbol: quantity}

    # Ask how many different stocks the user wants to enter.
    # try-except handles the case where the user types a
    # non-numeric value (like "five" instead of 5).
    while True:
        try:
            num_stocks = int(input("\nHow many stocks do you want to enter? "))

            # A negative or zero number does not make sense here.
            if num_stocks <= 0:
                print("Please enter a positive whole number.")
                continue  # ask again

            break  # valid number entered, exit the loop

        except ValueError:
            print("Invalid input! Please enter a whole number (e.g., 3).")

    # Loop 'num_stocks' times to collect each stock entry.
    count = 0
    while count < num_stocks:
        # Ask for the stock symbol and normalize it to uppercase
        # so that "aapl" and "AAPL" are treated the same.
        symbol = input("Enter stock symbol (e.g., AAPL): ").upper().strip()

        # Check if the entered stock exists in our stock_prices dictionary.
        if symbol not in stock_prices:
            print(f"'{symbol}' is not available. Please choose from the list above.")
            continue  # do not increase count, ask this entry again

        # Ask for the quantity, with exception handling for invalid numbers.
        try:
            quantity = int(input(f"Enter quantity for {symbol}: "))

            if quantity <= 0:
                print("Quantity must be a positive whole number.")
                continue  # ask this entry again

        except ValueError:
            print("Invalid input! Quantity must be a whole number.")
            continue  # ask this entry again

        # If the same stock is entered again, add to the existing quantity
        # instead of overwriting it (avoids losing earlier input).
        if symbol in portfolio:
            portfolio[symbol] += quantity
        else:
            portfolio[symbol] = quantity

        count += 1  # move on to the next stock entry

    return portfolio


# ---------------------------------------------------
# Function 3: calculate_portfolio()
# Purpose: Calculate the value of each stock holding and
#          the total investment value of the portfolio.
# Returns: (details_list, total_value)
#          details_list is a list of tuples:
#          (symbol, quantity, price, stock_value)
# ---------------------------------------------------
def calculate_portfolio(portfolio):
    details_list = []   # Will hold one tuple per stock
    total_value = 0      # Running total of the whole portfolio

    # Loop through each stock the user entered.
    for symbol, quantity in portfolio.items():
        price = stock_prices[symbol]        # Look up the fixed price
        stock_value = price * quantity      # Basic arithmetic (multiplication)
        total_value += stock_value          # Add to the running total

        details_list.append((symbol, quantity, price, stock_value))

    return details_list, total_value


# ---------------------------------------------------
# Function 4: display_portfolio()
# Purpose: Print a neat, well-formatted summary table of
#          the user's portfolio and the total investment.
# ---------------------------------------------------
def display_portfolio(details_list, total_value):
    print("\n" + "=" * 55)
    print(" " * 15 + "PORTFOLIO SUMMARY")
    print("=" * 55)
    print(f"{'Symbol':<10}{'Quantity':<12}{'Price':<12}{'Value':>15}")
    print("-" * 55)

    # Loop through the calculated details and print each row.
    for symbol, quantity, price, stock_value in details_list:
        print(f"{symbol:<10}{quantity:<12}{price:<12}{stock_value:>15}")

    print("-" * 55)
    print(f"{'TOTAL INVESTMENT VALUE:':<34}{total_value:>21}")
    print("=" * 55)


# ---------------------------------------------------
# Function 5: save_to_file()
# Purpose: Save the portfolio summary to a plain text file
#          (portfolio.txt) using file handling.
# ---------------------------------------------------
def save_to_file(details_list, total_value, filename="portfolio.txt"):
    try:
        # "w" mode creates the file if it doesn't exist,
        # or overwrites it if it already does.
        with open(filename, "w") as file:
            file.write("STOCK PORTFOLIO SUMMARY\n")
            file.write("=" * 55 + "\n")
            file.write(f"{'Symbol':<10}{'Quantity':<12}{'Price':<12}{'Value':>15}\n")
            file.write("-" * 55 + "\n")

            for symbol, quantity, price, stock_value in details_list:
                file.write(f"{symbol:<10}{quantity:<12}{price:<12}{stock_value:>15}\n")

            file.write("-" * 55 + "\n")
            file.write(f"TOTAL INVESTMENT VALUE: {total_value}\n")

        print(f"\nPortfolio successfully saved to '{filename}'.")

    except IOError:
        # This runs if the file could not be created/written for some reason
        # (e.g., no write permission on the folder).
        print(f"Error: Could not save the file '{filename}'.")


# ---------------------------------------------------
# Function 5b: save_to_csv() (Optional extra feature)
# Purpose: Save the portfolio summary as a CSV file
#          (portfolio.csv) so it can be opened in Excel.
# ---------------------------------------------------
def save_to_csv(details_list, total_value, filename="portfolio.csv"):
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            # Write the header row.
            writer.writerow(["Symbol", "Quantity", "Price", "Value"])

            # Write one row per stock.
            for symbol, quantity, price, stock_value in details_list:
                writer.writerow([symbol, quantity, price, stock_value])

            # Write the total as the last row.
            writer.writerow([])
            writer.writerow(["Total Investment Value", "", "", total_value])

        print(f"Portfolio successfully saved to '{filename}'.")

    except IOError:
        print(f"Error: Could not save the file '{filename}'.")


# ---------------------------------------------------
# Function 6: main()
# Purpose: Controls the overall flow of the program by
#          calling the other functions in the correct order.
# ---------------------------------------------------
def main():
    print("=" * 55)
    print(" " * 12 + "STOCK PORTFOLIO TRACKER")
    print("=" * 55)

    # Step 1: Show the user which stocks are available.
    display_available_stocks()

    # Step 2: Collect the user's stock choices and quantities.
    portfolio = get_stock_input()

    # Step 3: Calculate the value of each stock and the total.
    details_list, total_value = calculate_portfolio(portfolio)

    # Step 4: Display a formatted summary on the screen.
    display_portfolio(details_list, total_value)

    # Step 5: Ask the user if they want to save the results.
    save_choice = input("\nDo you want to save this portfolio to a file? (yes/no): ").lower().strip()

    if save_choice == "yes":
        # Always save the plain text version.
        save_to_file(details_list, total_value, "portfolio.txt")

        # Ask separately about the optional CSV file.
        csv_choice = input("Also save as CSV (portfolio.csv)? (yes/no): ").lower().strip()
        if csv_choice == "yes":
            save_to_csv(details_list, total_value, "portfolio.csv")
    else:
        print("Portfolio was not saved.")

    print("\nThank you for using Stock Portfolio Tracker!")


# ---------------------------------------------------
# Program entry point.
# This ensures main() runs only when this file is
# executed directly (not when imported elsewhere).
# ---------------------------------------------------
if __name__ == "__main__":
    main()C:/Users/harsh/OneDrive/Pictures/Screenshots/Screenshot 2026-07-01 192439.pngC:/Users/harsh/OneDrive/Pictures/Screenshots/Screenshot 2026-07-01 192439.png
