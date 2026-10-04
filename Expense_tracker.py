import csv
fp = open("expense_tracker.csv", "a", newline="")
file_writer = csv.writer(fp)
n = int(input("Enter the total no. of records "))
for i in range(n):
    Date = input("Date:")
    Expense = input("Expense")
    desc =input("Description ")
    Amt = input("Amount ")
    row = [Date,Expense,desc,Amt]
    file_writer.writerow(row)
    print("Record ",i+1," added ")
fp.close()