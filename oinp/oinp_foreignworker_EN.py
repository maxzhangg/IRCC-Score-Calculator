import tkinter as tk
from tkinter import ttk

# Scoring rules based on stream documentation
scoring_rules_fw = {
    "Job Offer: NOC TEER Category": {
        "NOC TEER 0 or 1": 10,
        "NOC TEER 2 or 3": 8,
        "NOC TEER 4": 0,
        "NOC TEER 5": 0
    },
    "Job Offer: NOC Occupational Category": {
        "Occupational Category 0, 2, 3": 10,
        "Occupational Category 7": 7,
        "Occupational Category 1, 9": 5,
        "Occupational Category 4, 8": 4,
        "Occupational Category 5, 6": 3
    },
    "Job Offer: Hourly Wage": {
        "$40/hour or higher": 10,
        "$35–$39.99/hour": 8,
        "$30–$34.99/hour": 7,
        "$25–$29.99/hour": 6,
        "$20–$24.99/hour": 5,
        "Less than $20/hour": 0
    },
    "Work Permit Status": {
        "With valid work permit": 10,
        "Without valid work permit": 0
    },
    "Job Tenure with Employer": {
        "6+ months working in job offer position": 3,
        "Less than 6 months / not currently working": 0
    },
    "Earnings History (CRA)": {
        "Annual income ≥ $40,000": 3,
        "Less than $40,000": 0
    },
    "Official Language Ability (CLB)": {
        "CLB 9 or higher": 10,
        "CLB 8": 6,
        "CLB 7": 4,
        "CLB 6 or lower": 0
    },
    "Knowledge of Official Languages": {
        "2 Official Languages": 10,
        "1 Official Language": 5
    },
    "Regionalization – Job Location": {
        "Northern Ontario": 10,
        "Other areas outside GTA": 8,
        "Inside GTA (excluding Toronto)": 3,
        "Toronto": 0
    }
}

def main():
    root = tk.Tk()
    root.title("OINP Foreign Worker Stream Scoring Tool")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")

    variables = {}
    row = 0

    for category, options in scoring_rules_fw.items():
        ttk.Label(frame, text=category).grid(row=row, column=0, sticky="w", pady=5)
        var = tk.StringVar()
        variables[category] = var
        combo = ttk.Combobox(frame, textvariable=var, values=list(options.keys()), state="readonly", width=55)
        combo.grid(row=row, column=1, pady=5)
        row += 1

    result_var = tk.StringVar(value="Total Score: 0")
    ttk.Label(frame, textvariable=result_var, font=("Arial", 12, "bold")).grid(row=row, columnspan=2, pady=10)

    def calculate_score():
        total = 0
        for cat, var in variables.items():
            choice = var.get()
            if choice in scoring_rules_fw[cat]:
                total += scoring_rules_fw[cat][choice]
        result_var.set(f"Total Score: {total}")

    ttk.Button(frame, text="Calculate Score", command=calculate_score).grid(row=row+1, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
