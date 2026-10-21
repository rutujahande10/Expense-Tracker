# CLI Expense Tracker

## Description

A Python command-line application for managing daily expenses.

## Features

- Add expenses with description, amount, and category.
- View all expenses.
- Filter expenses by category.
- Delete expenses by ID.
- Save expenses in a JSON file.
- Validate user input.

## Technologies

- Python 3
- JSON
- pathlib

## Project Structure

```text
Expense-Tracker/
├── main.py
├── expenses.json
├── README.md
└── .gitignore
```

## Requirements

Install Python 3.

Check the installation:

```bash
python --version
```

## How to Run

Open a terminal in the project directory and execute:

```bash
python main.py
```

## Menu Options

1. Add Expense
2. View All Expenses
3. Filter by Category
4. Delete Expense
5. Exit

## Data Storage

Expense records are stored in `expenses.json` and persist between program runs.

## Input Validation

The program checks for empty descriptions, empty categories, invalid amounts, and invalid expense IDs.

## Assignment Status

Core expense tracker features implemented and tested.