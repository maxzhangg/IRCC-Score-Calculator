import tkinter as tk
from tkinter import ttk

# Scoring rules for PhD Graduate Stream
scoring_rules_phd = {
    "Work or study permit status": {
        "With valid permit": 10,
        "Without valid permit": 0
    },
    "Earnings history": {
        "$40k or more in a year": 3,
        "Less than $40k in a year": 0
    },
    "Highest level of education": {
        "PhD": 10,
        "Masters": 8,
        "Bachelors or equivalent": 6,
        "Graduate diploma or certificate": 6,
        "Undergraduate diploma or certificate": 5,
        "Apprenticeship or trades certificate/diploma": 5,
        "Less than college or trade certificate": 0
    },
    "Field of study": {
        "STEM/Health/Trades": 12,
        "Business/Social Services/Education": 6,
        "Arts and Humanities": 0
    },
    "Canadian education experience": {
        "More than one Canadian credential": 10,
        "One Canadian credential": 5,
        "None": 0
    },
    "Official language ability": {
        "CLB 9 or higher": 10,
        "CLB 8": 6,
        "CLB 7": 4,
        "CLB 6 or lower": 0
    },
    "Knowledge of official languages": {
        "2 Official Languages (CLB 7+ & CLB 6+)": 10,
        "1 Official Language": 5,
        "None": 0
    },
    "Regionalization (Location of Study)": {
        "Northern Ontario": 10,
        "Outside GTA (not Northern Ontario)": 8,
        "Inside GTA (except Toronto)": 3,
        "Toronto": 0,
        "Completed without in-person classes": 0
    }
}

def main():
    root = tk.Tk()
    root.title("OINP PhD Graduate Stream Scoring Tool")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")

    variables = {}
    row = 0

    for category, options in scoring_rules_phd.items():
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
            if choice in scoring_rules_phd[cat]:
                total += scoring_rules_phd[cat][choice]
        result_var.set(f"Total Score: {total}")

    ttk.Button(frame, text="Calculate Total Score", command=calculate_score).grid(row=row+1, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()