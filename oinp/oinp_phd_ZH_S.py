import tkinter as tk
from tkinter import ttk

scoring_rules_phd = {
    "工作或学习许可状态": {
        "有有效工作或学习许可": 10,
        "没有有效许可": 0
    },
    "收入历史（过去5年报税）": {
        "年收入 $40,000 或以上": 3,
        "年收入少于 $40,000": 0
    },
    "最高学历": {
        "博士": 10,
        "硕士": 8,
        "学士或同等学历": 6,
        "研究生文凭或证书": 6,
        "本科学历或证书": 5,
        "学徒/技工证书或文凭": 5,
        "低于大专或技工证书": 0
    },
    "学习领域": {
        "STEM/健康/技工类": 12,
        "商科/教育/社会科学/法律等": 6,
        "人文艺术/社科（BHASE类）": 0
    },
    "加拿大教育经历": {
        "两个或以上加拿大学历": 10,
        "一个加拿大学历": 5
    },
    "官方语言能力（单语CLB）": {
        "CLB 9 或以上": 10,
        "CLB 8": 6,
        "CLB 7": 4,
        "CLB 6 或以下": 0
    },
    "官方语言掌握（双语）": {
        "掌握2种官方语言（CLB 7+ & CLB 6+）": 10,
        "掌握1种官方语言": 5
    },
    "学习地区（实际出席）": {
        "安省北部": 10,
        "GTA以外地区（不含北部）": 8,
        "GTA地区（不含多伦多）": 3,
        "多伦多": 0,
        "未线下出席课程": 0
    }
}

def main():
    if tk._default_root is None:
        root = tk.Tk()
    else:
        root = tk.Toplevel()
    root.title("OINP 博士毕业生类别打分器")

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

    result_var = tk.StringVar(value="总分: 0")
    ttk.Label(frame, textvariable=result_var, font=("Arial", 12, "bold")).grid(row=row, columnspan=2, pady=10)

    def calculate_score():
        total = 0
        for cat, var in variables.items():
            choice = var.get()
            if choice in scoring_rules_phd[cat]:
                total += scoring_rules_phd[cat][choice]
        result_var.set(f"总分: {total}")

    ttk.Button(frame, text="计算总分", command=calculate_score).grid(row=row+1, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()