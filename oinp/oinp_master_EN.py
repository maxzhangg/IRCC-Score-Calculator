import tkinter as tk
from tkinter import ttk

scoring_rules = {
    "Work or Study Permit Status": {
        "With valid work or study permit": 10,
        "Without valid permit": 0
    },
    "Earnings History": {
        "Annual income ≥ $40,000": 3,
        "Less than $40,000": 0
    },
    "Highest Level of Education": {
        "PhD": 10,
        "Master’s": 8,
        "Bachelor’s or equivalent": 6,
        "Graduate diploma or certificate": 6,
        "Undergraduate diploma or certificate": 5,
        "Apprenticeship/trades certificate or diploma": 5,
        "Less than college level": 0
    },
    "Field of Study": {
        "STEM / Health / Trades": 12,
        "Business / Education / Social Sciences / Services": 6,
        "Arts / Humanities / BHASE n.e.c.": 0
    },
    "Canadian Education Experience": {
        "More than one Canadian credential": 10,
        "One Canadian credential": 5,
        "None": 0
    },
    "Official Language Proficiency (CLB Level)": {
        "CLB 9 or higher": 10,
        "CLB 8": 6,
        "CLB 7": 4,
        "CLB 6 or lower": 0
    },
    "Knowledge of Official Languages": {
        "Proficient in both official languages (CLB7 + CLB6)": 10,
        "Proficient in one official language": 5,
        "Not proficient": 0
    },
    "Location of Study in Ontario": {
        "Northern Ontario": 10,
        "Outside GTA (not Northern Ontario)": 8,
        "Inside GTA (excluding Toronto)": 3,
        "Toronto": 0,
        "Remote study (no in-person classes)": 0
    }
}

def main():
    if tk._default_root is None:
        root = tk.Tk()
    else:
        root = tk.Toplevel()
    root.title("OINP Masters Stream Scoring Tool")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")

    variables = {}
    row = 0

    for category, options in scoring_rules.items():
        ttk.Label(frame, text=category).grid(row=row, column=0, sticky="w", pady=5)
        var = tk.StringVar()
        variables[category] = var
        combo = ttk.Combobox(frame, textvariable=var, values=list(options.keys()), state="readonly", width=45)
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
