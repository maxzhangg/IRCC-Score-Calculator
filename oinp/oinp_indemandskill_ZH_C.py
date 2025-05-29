import tkinter as tk
from tkinter import ttk

scoring_rules_yue = {
    "職位所屬職業大類（NOC）": {
        "0/2/3 類": 10,
        "第7類": 7,
        "第1或第9類": 5,
        "第4或第8類": 4,
        "第5或第6類": 3
    },
    "工資水平（每小時）": {
        "$40 或以上": 10,
        "$35 - $39.99": 8,
        "$30 - $34.99": 7,
        "$25 - $29.99": 6,
        "$20 - $24.99": 5,
        "少過 $20": 0
    },
    "工簽狀態": {
        "持有有效工作簽證": 10,
        "冇有效簽證": 0
    },
    "喺現職崗位工作時間": {
        "6個月或以上": 3,
        "少過6個月或者未開始": 0
    },
    "加拿大工作經驗 - 收入記錄": {
        "單一年份收入 ≥ $40,000": 3,
        "單一年份收入 < $40,000": 0
    },
    "職位地點（地區移民）": {
        "安省北部": 10,
        "GTA以外地區（唔包括北部）": 8,
        "GTA區域（唔包括多倫多）": 3,
        "多倫多": 0
    }
}

def main():
    if tk._default_root is None:
        root = tk.Tk()
    else:
        root = tk.Toplevel()
    root.title("OINP 僱主擔保 - 緊缺技能類別打分器（粵語版）")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")

    variables = {}
    row = 0

    for category, options in scoring_rules_yue.items():
        ttk.Label(frame, text=category).grid(row=row, column=0, sticky="w", pady=5)
        var = tk.StringVar()
        variables[category] = var
        combo = ttk.Combobox(frame, textvariable=var, values=list(options.keys()), state="readonly", width=50)
        combo.grid(row=row, column=1, pady=5)
        row += 1

    result_var = tk.StringVar(value="總分: 0")
    ttk.Label(frame, textvariable=result_var, font=("Arial", 12, "bold")).grid(row=row, columnspan=2, pady=10)

    def calculate_score():
        total = 0
        for cat, var in variables.items():
            choice = var.get()
            if choice in scoring_rules_yue[cat]:
                total += scoring_rules_yue[cat][choice]
        result_var.set(f"總分: {total}")

    ttk.Button(frame, text="計算總分", command=calculate_score).grid(row=row+1, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
