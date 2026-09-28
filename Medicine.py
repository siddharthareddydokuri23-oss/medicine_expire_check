import datetime
import csv
class Medicine:
    def __init__(self, name, expiry_date, price):
        self.name = name
        self.expiry_date = datetime.datetime.strptime(expiry_date, "%Y-%m-%d")
        self.price = price
    def is_expired(self):
        return datetime.datetime.now() > self.expiry_date
    def status(self):
        if self.is_expired():
            return "Expired"
        elif (self.expiry_date - datetime.datetime.now()).days <= 7:
            return "Near Expiry"
        else:
            return "Available"
def add_expense(category, amount):
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([category, amount])
def view_expenses():
    print("\n--- Expense Report ---")
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Category: {row[0]}, Amount: {row[1]}")
if __name__ == "__main__":
    meds = [
        Medicine("Paracetamol", "2026-10-05", 50),
        Medicine("Amoxicillin", "2026-09-20", 120),
        Medicine("Ibuprofen", "2026-10-15", 80),
    ]
    print("\n--- Medicine Status ---")
    for m in meds:
        print(f"{m.name}: {m.status()} (₹{m.price})")
    add_expense("Medicine Purchase", 250)
    add_expense("Transport", 100)
    view_expenses()