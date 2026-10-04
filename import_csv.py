import csv
from datetime import datetime
from connect import con, cursor

count = 0
with open("expense_tracker.csv", newline="") as f:
    for row in csv.reader(f):
        if len(row) < 4:
            continue
        date_str, category, description, amount = row[:4]
        try:
            amount = float(amount)
            date = datetime.strptime(date_str.strip(), "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            print("Skipped:", row)      # header row or bad data
            continue
        cursor.execute(
            "INSERT INTO expenses (expense_date, category, description, amount) VALUES (%s, %s, %s, %s)",
            (date, category.strip(), description.strip(), amount)
        )
        count += 1

con.commit()
print(count, "rows imported")