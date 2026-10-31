# stock-portfolio-2026-
# 📈 Stock Portfolio Tracker – Python Project

## 📌 Project Overview

The Stock Portfolio Tracker is a beginner-friendly, command-line-based Python application developed as part of the **CodeAlpha Python Programming Internship – Task 2**.

This program allows users to create and manage a simple stock portfolio using predefined stock prices. It calculates the investment value of each stock and the total portfolio value.

The user can also save the portfolio summary in a text file or CSV file for future reference.

## 🎯 Objectives

- To develop a stock portfolio tracking application using Python.
- To understand dictionaries, functions, and loops.
- To perform calculations using stock prices and quantities.
- To implement input validation and exception handling.
- To understand file handling and CSV operations.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Module:** CSV (Built-in Python Module)
- **Platform:** Command-Line Interface (CLI)
- **File Formats:** TXT and CSV

## ✨ Features

1. **Available Stocks:** Displays five predefined stocks with their prices.
2. **Stock Selection:** Allows users to select stocks using their symbols.
3. **Quantity Input:** Accepts the number of shares for each stock.
4. **Input Validation:** Handles invalid stock symbols and incorrect quantities.
5. **Portfolio Calculation:** Calculates individual stock values and total investment.
6. **Portfolio Summary:** Displays a formatted portfolio report.
7. **Text File Export:** Saves portfolio details in `portfolio.txt`.
8. **CSV Export:** Exports portfolio details into `portfolio.csv`, which can be opened in Excel.

## 📊 Available Stocks and Prices

| Stock Symbol | Price per Share |
|---|---:|
| AAPL | 180 |
| TSLA | 250 |
| GOOGL | 140 |
| MSFT | 420 |
| AMZN | 190 |

*Note: These are fixed sample prices defined in the program, not live market prices.*

## ⚙️ Functions Used

| Function | Description |
|---|---|
| `display_available_stocks()` | Displays available stocks and prices. |
| `get_stock_input()` | Collects stock symbols and quantities. |
| `calculate_portfolio()` | Calculates individual and total investment values. |
| `display_portfolio()` | Displays the portfolio summary. |
| `save_to_file()` | Saves portfolio details in a text file. |
| `save_to_csv()` | Saves portfolio details in CSV format. |
| `main()` | Controls the overall program execution. |

## 🧮 Calculation Formula

**Individual Stock Value:**

Stock Value = Price per Share × Quantity

**Total Investment Value:**

Total Investment = Sum of all Individual Stock Values

### Example

- AAPL: 180 × 10 = 1800
- TSLA: 250 × 5 = 1250
- MSFT: 420 × 2 = 840

**Total Investment Value = 3890**

## ▶️ How to Run the Project

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code or a terminal.
4. Save the Python program as `stock_portfolio.py`.
5. Execute the following command:

```bash
python stock_portfolio.py
```

6. View the available stocks.
7. Enter the stock symbols and quantities.
8. View the calculated portfolio summary.
9. Choose whether to save the results as TXT and CSV files.

## 📁 Project Structure

```text
Stock-Portfolio-Tracker/
│
├── stock_portfolio.py
├── portfolio.txt
├── portfolio.csv
└── README.md
```

*The TXT and CSV files are generated when the user chooses to save the portfolio.*

## 📚 Python Concepts Used

- Variables and Data Types
- Dictionaries
- Functions
- For Loops and While Loops
- Conditional Statements
- Exception Handling (`try-except`)
- User Input (`input()`)
- String Formatting
- File Handling
- CSV Module

## 🚀 Future Enhancements

- Integrate live stock market prices using an API.
- Add graphical user interface (GUI).
- Include stock price history and performance charts.
- Add user login and portfolio management.
- Implement investment profit and loss calculations.

## 🏁 Conclusion

The Stock Portfolio Tracker is a simple Python application that helps users calculate and maintain a basic stock investment portfolio. This project provides practical knowledge of Python programming concepts, including functions, dictionaries, exception handling, calculations, and file handling.

It demonstrates how Python can be used to develop useful real-world applications.

---

**Project Name:** Stock Portfolio Tracker  
**Internship:** CodeAlpha – Python Programming Internship  
**Task:** Task 2  
**Programming Language:** Python  
**Project Type:** Command-Line Application
