💰 Expense Tracker

A simple Expense Tracker built using Python, Pandas, and Matplotlib that helps you visualize your daily spending habits with bar and pie charts.
📘 Project Overview

The Expense Tracker is designed to help users monitor their daily expenses by category.
It loads data from a CSV file, calculates the total spending, and visualizes spending distribution using bar and pie charts.

🗂️ Project Structure
ExpenseTracker/
│
├── data/
│   └── expenses.csv         # Sample expense data
│
├── app.py                   # Main Python application
│
├── requirements.txt         # Dependencies list
│
└── README.md                # Project documentation

⚙️ Features
✅ Load expenses from a CSV file
✅ Calculate total spending
✅ Display category-wise spending summary
✅ Generate visualizations (bar chart + pie chart)
✅ Easy to extend for adding new features like:

Date filters

Monthly reports

GUI or web interface
💾 Sample Data (data/expenses.csv)
Date,Category,Amount,Description
2025-10-01,Food,250,Lunch at canteen
2025-10-02,Travel,120,Bus fare
2025-10-03,Shopping,500,Clothes
🧠 How It Works

The program reads data/expenses.csv using Pandas.

It calculates:

Total spending

Spending by category

It displays results in the console.

It generates:

spending_bar_chart.png

spending_pie_chart.png
🛠️ Installation & Setup
Step 1: Clone the Repository
git clone https://github.com/your-username/ExpenseTracker.git
cd ExpenseTracker

Step 2: Create Virtual Environment
python -m venv .venv

Step 3: Activate the Environment
On Windows (PowerShell)
.venv\Scripts\Activate.ps1

On macOS / Linux
source .venv/bin/activate

Step 4: Install Dependencies
pip install -r requirements.txt

Step 5: Run the Application
python app.py
📊 Output Example

Console Output:

📄 Expense Data:
         Date  Category  Amount       Description
0  2025-10-01      Food     250  Lunch at canteen
1  2025-10-02    Travel     120          Bus fare
2  2025-10-03  Shopping     500           Clothes

💰 Total Spent: 870


Generated Files:

spending_bar_chart.png

spending_pie_chart.png

🧩 Requirements

Python 3.8+

pandas

matplotlib

Add these to requirements.txt:
pandas
matplotlib
