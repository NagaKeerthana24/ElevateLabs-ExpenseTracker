import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------- STEP 1: Load or create expense file ----------
csv_path = os.path.join("data", "expenses.csv")

# Create data folder if not present
os.makedirs("data", exist_ok=True)

if not os.path.exists(csv_path):
    df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
    df.to_csv(csv_path, index=False)
    print("✅ Created new expenses.csv file.")
else:
    df = pd.read_csv(csv_path)

    # Fix incorrectly formatted CSVs (merged columns)
    if len(df.columns) == 1 and "," in df.columns[0]:
        df = df[df.columns[0]].str.split(",", expand=True)
        df.columns = ["Date", "Category", "Amount", "Description"]

    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

print("\n📄 Current Expenses:")
print(df.head())

# ---------- STEP 2: Add new expense ----------
choice = input("\nWould you like to add a new expense? (yes/no): ").strip().lower()

if choice == "yes":
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food/Travel/Shopping/etc.): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    new_entry = pd.DataFrame([[date, category, amount, description]],
                             columns=["Date", "Category", "Amount", "Description"])

    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(csv_path, index=False)
    print("\n✅ Expense added successfully!")

# ---------- STEP 3: Summary ----------
total_spent = df["Amount"].sum()
category_summary = df.groupby("Category")["Amount"].sum()

print("\n💰 Total Spent:", total_spent)
print("\n📊 Spending by Category:\n", category_summary)

# ---------- STEP 4: Visuals ----------
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.pie(category_summary, labels=category_summary.index, autopct='%1.1f%%', startangle=90)
plt.title("Expense Distribution by Category")

plt.subplot(1, 2, 2)
category_summary.plot(kind="bar", color="skyblue")
plt.title("Expense by Category")
plt.xlabel("Category")
plt.ylabel("Amount (₹)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# ---------- STEP 5: Export to Excel ----------
os.makedirs("reports", exist_ok=True)
excel_path = os.path.join("reports", "Expense_Report.xlsx")

with pd.ExcelWriter(excel_path) as writer:
    df.to_excel(writer, sheet_name="Expenses", index=False)
    category_summary.to_excel(writer, sheet_name="Summary")

print(f"\n📤 Data exported successfully to {excel_path}")
