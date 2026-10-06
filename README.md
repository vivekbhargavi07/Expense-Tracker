# 💰 Expense Tracker

A Python application to record, organize, and review personal expenses. It supports bulk-loading expenses from CSV files and is being extended to store data in a MySQL database.

> My first GitHub project, built while transitioning from operations into IT and data roles.

## 📌 Features

- Record and manage personal expenses using Python
- Import expenses in bulk from a CSV file with `import_csv.py`
- 🚧 In progress: moving storage from CSV to a MySQL database

## 🗂️ Project Structure

```
Expense-Tracker/
├── Expense_tracker.py   # Main application
├── import_csv.py        # Imports expenses from a CSV file
└── README.md
```

## 🛠️ Tech Stack

- Python 3
- CSV (current storage and import)
- MySQL (integration in progress)

## ⚙️ Getting Started

```bash
git clone https://github.com/vivekbhargavi07/Expense-Tracker.git
cd Expense-Tracker
python Expense_tracker.py
```

To import expenses from a CSV file:

```bash
python import_csv.py
```

For the MySQL version, install the connector:

```bash
pip install mysql-connector-python
```

## 🗺️ Roadmap

- [x] Basic expense tracking in Python
- [x] CSV import
- [ ] Store data in MySQL instead of CSV
- [ ] Monthly and category-wise reports
- [ ] Dashboard in Power BI on top of the data

## 📚 What I Learned

- Structuring a Python project into separate scripts
- Reading and writing CSV data
- Connecting Python to a MySQL database
- Using Git and GitHub for version control

## 👩‍💻 Author

**Bhargavi Vivek**
Operations & Process Analyst moving into IT | SQL · Python · Power BI · Advanced Excel

[GitHub](https://github.com/vivekbhargavi07)

Feedback and suggestions are welcome!
