import tkinter as tk
from tkinter import ttk

# 粤语版：OINP 雇主担保 - 海外工人类别打分项
scoring_rules = {
    "工作职位：NOC TEER 类别": {
        "TEER 0 或 1": 10,
        "TEER 2 或 3": 8,
        "TEER 4": 0,
        "TEER 5": 0
    },
    "工作职位：NOC 职业大类": {
        "职业大类 0 / 2 / 3": 10,
        "职业大类 7": 7,
        "职业大类 1 / 9": 5,
        "职业大类 4 / 8": 4,
        "职业大类 5 / 6": 3
    },
    "工资水平（每小时）": {
        "每小时 ≥ $40": 10,
        "$35 - $39.99": 8,
        "$30 - $34.99": 7,
        "$25 - $29.99": 6,
        "$20 - $24.99": 5,
        "低于 $20": 0
    },
    "工作签证状态": {
        "持有有效工作签证": 10,
        "冇有效签证": 0
    },
    "目前是否喺呢份工作岗位工作超过6个月": {
        "喺安省该岗位工作满6个月或以上": 3,
        "少于6个月或未开始工作": 0
    },
    "加拿大工作经验（年收入）": {
        "年收入 ≥ $40,000": 3,
        "年收入 < $40,000": 0
    },
    "官方语言能力（CLB）": {
        "CLB 9 或以上": 10,
        "CLB 8": 6,
        "CLB 7": 4,
        "CLB 6 或以下": 0
    },
    "官方语言知识": {
        "懂两种官方语言（CLB7+CLB6）": 10,
        "懂一种官方语言": 5
    },
    "工作地点（区域化）": {
        "安省北部": 10,
        "GTA 以外地区（唔包北部）": 8,
        "GTA 内但唔系多伦多": 3,
        "多伦多": 0
    }
}

def main():
    if tk._default_root is None:
        root = tk.Tk()
    else:
        root = tk.Toplevel()
    root.title("OINP 雇主担保 - 海外工人类别打分器（粵語）")

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

    result_var = tk.StringVar(value="總分: 0")
    ttk.Label(frame, textvariable=result_var, font=("Arial", 12, "bold")).grid(row=row, columnspan=2, pady=10)

    def calculate_score():
        total = 0
        for cat, var in variables.items():
            choice = var.get()
            if choice in scoring_rules[cat]:
                total += scoring_rules[cat][choice]
        result_var.set(f"總分: {total}")

    ttk.Button(frame, text="計算總分", command=calculate_score).grid(row=row+1, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
