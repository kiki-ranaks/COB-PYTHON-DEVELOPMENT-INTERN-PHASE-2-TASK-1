# COB-PYTHON-DEVELOPMENT-INTERN-PHASE-2-TASK-1
# Expense Tracker

The Expense Tracker is a simple tool built using Python and the `tkinter` library to help you track and manage your personal expenses and generate monthly reports.

## Features

- Record daily expenses with date, category, description, and amount.
- Calculate and display total expenses for a specific month and year.
- User-friendly interface for easy data entry.
- Data validation for accurate input.
- Minimalist expense tracking tool.

## Usage

1. **Record an Expense:**

   - Enter the expense details in the provided input fields: date (YYYY-MM-DD), category, description, and amount ($).
   - Click the "Record Expense" button to save the expense.

2. **Generate a Monthly Report:**

   - Enter the year and month (1-12) for which you want to generate a report.
   - Click the "Generate Report" button to calculate and display the total expenses for the specified period.

3. **Data Persistence:**

   - The expenses are saved in a CSV file named "expenses.csv" for future reference.

4. **Clear Input Fields:**

   - After recording an expense, the input fields are cleared for convenience.

## Requirements

- Python (3.x recommended)
- The `tkinter` library is included with standard Python distributions.

## Installation

1. Clone this repository to your local machine or download the code.

2. Run the application by executing the Python script:

   ```bash
   python expense_tracker.py
