import tkinter as tk
from tkinter import ttk

# Scoring rules for OINP Employer Job Offer: In-Demand Skills stream
scoring_rules = {
    "Job Offer: NOC Broad Occupational Category": {
        "Occupational Category 0, 2, 3": 10,
        "Occupational Category 7": 7,
        "Occupational Category 1, 9": 5,
        "Occupational Category 4, 8": 4,
        "Occupational Category 5, 6": 3,
    },
    "Job Offer: Wage (Hourly)": {
        "$40 or more": 10,
        "$35 - $39.99": 8,
        "$30 - $34.99": 7,
        "$25 - $29.99": 6,
        "$20 - $24.99": 5,
        "Less than $20": 0
    },
    "Work Permit Status": {
        "Valid work permit": 10,
        "No valid permit": 0
    },
    "Job Tenure with Job Offer Employer": {
        "6 months or more in position": 3,
        "Less than 6 months or not started": 0
    },
    "Canadian Work Experience: Earnings History": {
        "$40k or more in a year": 3,
        "Less than $40k in a year": 0
    },
    "Location of Job Offer": {
        "Northern Ontario": 10,
        "Outside GTA (except Northern Ontario)": 8,
        "Inside GTA (except Toronto)": 3,
        "Toronto": 0
    }
}

def main():
    if tk._default_root is None:
        root = tk.Tk()
    else:
        root = tk.Toplevel()
    root.title("OINP In-Demand Skills Stream - Scoring Calculator")

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

    ttk.Button(frame, text="Calculate Total Score", command=calculate_score).grid(row=row+1, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
