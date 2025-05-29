import tkinter as tk
from tkinter import ttk

# 简体中文：OINP 雇主担保 - 留学生类别打分项
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
    "工签或学签状态": {
        "持有有效工签或学签": 10,
        "无有效签证": 0
    },
    "是否已在该岗位工作满6个月": {
        "工作满6个月及以上": 3,
        "少于6个月或未开始": 0
    },
    "加拿大收入记录（近五年）": {
        "年收入 ≥ $40,000": 3,
        "年收入 < $40,000": 0
    },
    "最高学历": {
        "博士": 10,
        "硕士": 8,
        "学士或同等": 6,
        "研究生文凭或证书": 6,
        "本科文凭或证书": 5,
        "技工/行业证书或文凭": 5,
        "低于大专": 0
    },
    "所学专业领域": {
        "STEM/健康/技工类": 12,
        "商业/法律/教育/服务类": 6,
        "人文/艺术/其他未分类": 0
    },
    "加拿大教育经历": {
        "多个加拿大学历": 10,
        "一个加拿大学历": 5,
        "无": 0
    },
    "语言能力（CLB）": {
        "CLB 9 或以上": 10,
        "CLB 8": 6,
        "CLB 7": 4,
        "CLB 6 或以下": 0
    },
    "官方语言掌握": {
        "两种语言（CLB7+CLB6）": 10,
        "一种语言": 5
    },
    "工作地点（区域化）": {
        "安省北部": 10,
        "GTA 以外地区（不含北部）": 8,
        "GTA 区域（不含多伦多）": 3,
        "多伦多": 0
    },
    "学习地点（区域化）": {
        "安省北部": 10,
        "GTA 以外地区（不含北部）": 8,
        "GTA 区域（不含多伦多）": 3,
        "多伦多": 0,
        "纯线上学习": 0
    }
}

def main():
    if tk._default_root is None:
        root = tk.Tk()
    else:
        root = tk.Toplevel()
    root.title("OINP 雇主担保 - 留学生类别打分器（简体中文）")

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
