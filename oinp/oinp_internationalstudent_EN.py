import tkinter as tk
from tkinter import ttk

# Define scoring options based on the International Student stream factors
scoring_rules = {
    "Job offer: NOC TEER category": {
        "TEER 0 or 1": 10,
        "TEER 2 or 3": 8,
        "TEER 4": 0,
        "TEER 5": 0
    },
    "Job offer: NOC occupational category": {
        "Category 0 / 2 / 3": 10,
        "Category 7": 7,
        "Category 1 / 9": 5,
        "Category 4 / 8": 4,
        "Category 5 / 6": 3
    },
    "Job offer wage (hourly)": {
        "$40 or more": 10,
        "$35 - $39.99": 8,
        "$30 - $34.99": 7,
        "$25 - $29.99": 6,
        "$20 - $24.99": 5,
        "Less than $20": 0
    },
    "Work or Study Permit Status": {
        "With valid permit": 10,
        "Without valid permit": 0
    },
    "Job Tenure (same position)": {
        "6 months or more": 3,
        "Less than 6 months or not working": 0
    },
    "Earnings History (CRA)": {
        "$40,000 or more in a year": 3,
        "Less than $40,000 in a year": 0
    },
    "Highest Level of Education": {
        "PhD": 10,
        "Master’s": 8,
        "Bachelor’s or equivalent": 6,
        "Graduate diploma or certificate": 6,
        "Undergraduate diploma or certificate": 5,
        "Trades/apprenticeship cert.": 5,
        "Less than college level": 0
    },
    "Field of Study": {
        "STEM / Health / Trades": 12,
        "Business / Education / Social Sciences": 6,
        "Arts / Humanities / BHASE": 0
    },
    "Canadian Education Experience": {
        "More than one Canadian credential": 10,
        "One Canadian credential": 5
    },
    "Official Language Ability (CLB)": {
        "CLB 9 or higher": 10,
        "CLB 8": 6,
        "CLB 7": 4,
        "CLB 6 or lower": 0
    },
    "Knowledge of Official Languages": {
        "2 Official Languages (CLB7 + CLB6)": 10,
        "1 Official Language": 5
    },
    "Location of Job Offer": {
        "Northern Ontario": 10,
        "Outside GTA (not Northern)": 8,
        "Inside GTA (except Toronto)": 3,
        "Toronto": 0
    },
    "Location of Study": {
        "Northern Ontario": 10,
        "Outside GTA (not Northern)": 8,
        "Inside GTA (except Toronto)": 3,
        "Toronto": 0,
        "Remote / No in-person": 0
    }
}

def main():
    if tk._default_root is None:
        root = tk.Tk()
    else:
        root = tk.Toplevel()
    root.title("OINP International Student Stream Scoring Tool")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")

    variables = {}
    row = 0

    for category, options in scoring_rules.items():
        ttk.Label(frame, text=category).grid(row=row, column=0, sticky="w", pady=5)
        var = tk.StringVar()
        variables[category] = var
        combo = ttk.Combobox(frame, textvariable=var, values=list(options.keys()), state="readonly", width=50)
        combo.grid(row=row, column=1, pady=5)
        row += 1

    result_var = tk.StringVar(value="Total Score: 0")
    ttk.Label(frame, textvariable=result_var, font=("Arial", 12, "bold")).grid(row=row, columnspan=2, pady=10)

    def calculate_score():
        total = 0
        for cat, var in variables.items():
            choice = var.get()
            if choice in scoring_rules[cat]:
                total += scoring_rules[cat][choice]
        result_var.set(f"Total Score: {total}")

    ttk.Button(frame, text="Calculate Score", command=calculate_score).grid(row=row+1, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
