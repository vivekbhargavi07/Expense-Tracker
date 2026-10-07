import csv
import os
from datetime import datetime
from connect import con, cursor

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "expense_tracker.csv")

count = 0
skipped = 0

with open(CSV_PATH, newline="") as f:
    for row in csv.reader(f):
        if len(row) < 4:
            continue

        date_str, category, description, amount = row[:4]
        category = category.strip()
        description = description.strip()

        try:
            amount = float(amount)
            expense_date = datetime.strptime(date_str.strip(), "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            print("Skipped:", row)      # header row or bad data
            continue

        # add the category to the parent table if it's new, then get its id
        cursor.execute(
            "INSERT IGNORE INTO categories (category_name) VALUES (%s)", (category,)
        )
        cursor.execute(
            "SELECT category_id FROM categories WHERE category_name = %s", (category,)
        )
        category_id = cursor.fetchone()[0]

        # INSERT IGNORE skips rows that already exist (needs the unique key)
        cursor.execute(
            "INSERT IGNORE INTO expenses "
            "(expense_date, category, category_id, description, amount) "
            "VALUES (%s, %s, %s, %s, %s)",
            (expense_date, category, category_id, description, amount)
        )

        if cursor.rowcount == 1:
            count += 1
        else:
            skipped += 1

con.commit()
print(count, "new rows imported,", skipped, "duplicates skipped")

