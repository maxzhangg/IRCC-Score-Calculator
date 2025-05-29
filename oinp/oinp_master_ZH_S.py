import tkinter as tk
from tkinter import ttk

scoring_rules = {
    "就业/劳动力市场因素": {
        "持有有效工作或学习许可": 10,
        "没有有效的许可": 0
    },
    "盈利历史": {
        "年收入 ≥ 40,000 CAD": 3,
        "年收入 < 40,000 CAD": 0
    },
    "教育 - 最高教育水平": {
        "博士": 10,
        "硕士": 8,
        "学士或同等": 6,
        "研究生文凭或证书": 6,
        "本科文凭或证书": 5,
        "学徒或行业证书": 5,
        "低于大专": 0
    },
    "教育 - 研究领域": {
        "STEM/健康/贸易": 12,
        "商业/教育/社会科学": 6,
        "人文艺术/未分类": 0
    },
    "加拿大教育经历": {
        "多个加拿大证书": 10,
        "一个加拿大证书": 5,
        "无": 0
    },
    "语言能力 - CLB 分数": {
        "CLB 9+": 10,
        "CLB 8": 6,
        "CLB 7": 4,
        "CLB 6 或以下": 0
    },
    "语言能力 - 官方语言知识": {
        "两种语言达到标准": 10,
        "一种语言达到标准": 5,
        "不满足": 0
    },
    "地区移民 - 学习地点": {
        "安省北部": 10,
        "非GTA地区": 8,
        "GTA除多伦多": 3,
        "多伦多": 0,
        "纯线上": 0
    }
}

def main():
    root = tk.Tk()
    root.title("OINP 硕士类打分器")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")

    variables = {}
    row = 0

    for category, options in scoring_rules.items():
        ttk.Label(frame, text=category).grid(row=row, column=0, sticky="w", pady=5)
        var = tk.StringVar()
        variables[category] = var
        combo = ttk.Combobox(frame, textvariable=var, values=list(options.keys()), state="readonly", width=30)
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
