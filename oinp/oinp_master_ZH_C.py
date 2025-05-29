import tkinter as tk
from tkinter import ttk

scoring_rules = {
    "就業／勞動市場因素": {
        "持有有效工作或學生簽證": 10,
        "冇有效簽證": 0
    },
    "盈利紀錄": {
        "年收入 ≥ 40,000 加元": 3,
        "年收入 < 40,000 加元": 0
    },
    "教育程度（最高）": {
        "博士": 10,
        "碩士": 8,
        "學士或同等學歷": 6,
        "研究生文憑／證書": 6,
        "本科文憑／證書": 5,
        "學徒或行業證書": 5,
        "低於專上教育": 0
    },
    "教育範疇": {
        "STEM／醫療／技術行業": 12,
        "商業／教育／社會科學": 6,
        "人文藝術／未分類": 0
    },
    "加拿大教育經驗": {
        "多個加國學歷證書": 10,
        "一個加國學歷證書": 5,
        "冇": 0
    },
    "語言能力（CLB 等級）": {
        "CLB 9 或以上": 10,
        "CLB 8": 6,
        "CLB 7": 4,
        "CLB 6 或以下": 0
    },
    "官方語言能力": {
        "兩種官方語言都達標": 10,
        "一種官方語言達標": 5,
        "唔達標": 0
    },
    "讀書地點（地區移民）": {
        "安省北部": 10,
        "非GTA地區": 8,
        "GTA（唔包括多倫多）": 3,
        "多倫多": 0,
        "純網上課程": 0
    }
}

def main():
    if tk._default_root is None:
        root = tk.Tk()
    else:
        root = tk.Toplevel()
    root.title("OINP 碩士類打分器（粵語版）")

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
