import tkinter as tk
from tkinter import ttk

scoring_rules = {
    "职位类别（NOC TEER）": {
        "TEER 0 或 1": 10,
        "TEER 2 或 3": 8,
        "TEER 4": 0,
        "TEER 5": 0
    },
    "职业大类（NOC大类）": {
        "0、2、3 类职业": 10,
        "7 类职业": 7,
        "1、9 类职业": 5,
        "4、8 类职业": 4,
        "5、6 类职业": 3
    },
    "职位薪资（时薪）": {
        "每小时 $40 及以上": 10,
        "$35 - $39.99": 8,
        "$30 - $34.99": 7,
        "$25 - $29.99": 6,
        "$20 - $24.99": 5,
        "低于 $20": 0
    },
    "工签状态": {
        "持有有效工签": 10,
        "无有效工签": 0
    },
    "当前在岗时长": {
        "已在该岗位工作 ≥ 6 个月": 3,
        "少于 6 个月或未开始工作": 0
    },
    "加拿大工作经历（近5年收入）": {
        "某一年收入 ≥ $40,000": 3,
        "收入低于 $40,000": 0
    },
    "官方语言能力（CLB）": {
        "CLB 9 或以上": 10,
        "CLB 8": 6,
        "CLB 7": 4,
        "CLB 6 或以下": 0
    },
    "官方语言种类": {
        "掌握两种官方语言": 10,
        "掌握一种官方语言": 5
    },
    "工作地点区域": {
        "安省北部": 10,
        "非GTA其他地区（不含北部）": 8,
        "GTA内（不含多伦多）": 3,
        "多伦多市": 0
    }
}

def main():
    if tk._default_root is None:
        root = tk.Tk()
    else:
        root = tk.Toplevel()
    root.title("OINP 雇主担保：海外劳工类别打分器")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")

    variables = {}
    row = 0

    for category, options in scoring_rules.items():
        ttk.Label(frame, text=category).grid(row=row, column=0, sticky="w", pady=5)
        var = tk.StringVar()
        variables[category] = var
        combo = ttk.Combobox(frame, textvariable=var, values=list(options.keys()), state="readonly", width=35)
        combo.grid(row=row, column=1, pady=5)
        row += 1

    result_var = tk.StringVar(value="总分: 0")
    ttk.Label(frame, textvariable=result_var, font=("Arial", 12, "bold")).grid(row=row, columnspan=2, pady=10)

    def calculate_score():
        total = 0
        for cat, var in variables.items():
            choice = var.get()
            if choice in scoring_rules[cat]:
                total += scoring_rules[cat][choice]
        result_var.set(f"总分: {total}")

    ttk.Button(frame, text="计算总分", command=calculate_score).grid(row=row+1, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
