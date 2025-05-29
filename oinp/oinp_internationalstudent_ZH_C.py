import tkinter as tk
from tkinter import ttk

# OINP 雇主擔保：國際學生類別 - 粵語打分項
scoring_rules = {
    "工作職位：NOC TEER 類別": {
        "TEER 0 或 1": 10,
        "TEER 2 或 3": 8,
        "TEER 4": 0,
        "TEER 5": 0
    },
    "工作職位：NOC 職業大類": {
        "大類 0 / 2 / 3": 10,
        "大類 7": 7,
        "大類 1 / 9": 5,
        "大類 4 / 8": 4,
        "大類 5 / 6": 3
    },
    "工資水平（每小時）": {
        "≥ $40/hr": 10,
        "$35 - $39.99/hr": 8,
        "$30 - $34.99/hr": 7,
        "$25 - $29.99/hr": 6,
        "$20 - $24.99/hr": 5,
        "少過 $20/hr": 0
    },
    "工作或學生簽證狀態": {
        "持有效簽證": 10,
        "冇有效簽證": 0
    },
    "喺提供工作崗位工作咗幾耐": {
        "6個月或以上": 3,
        "少於6個月／未開始": 0
    },
    "稅單顯示收入（近5年）": {
        "年收入 ≥ $40,000": 3,
        "年收入 < $40,000": 0
    },
    "最高教育程度": {
        "博士": 10,
        "碩士": 8,
        "學士或同等": 6,
        "研究生文憑／證書": 6,
        "本科文憑／證書": 5,
        "學徒／行業證書": 5,
        "低於專上水平": 0
    },
    "專業領域": {
        "STEM／健康／技術行業": 12,
        "商科／教育／社會科學等": 6,
        "人文／藝術等其他": 0
    },
    "加拿大教育經歷": {
        "多於一個學歷": 10,
        "一個學歷": 5
    },
    "官方語言能力（CLB）": {
        "CLB 9 或以上": 10,
        "CLB 8": 6,
        "CLB 7": 4,
        "CLB 6 或以下": 0
    },
    "官方語言知識": {
        "兩種官方語言達標": 10,
        "一種官方語言達標": 5
    },
    "工作地點": {
        "安省北部": 10,
        "GTA 外（不包北部）": 8,
        "GTA 內（唔包括多倫多）": 3,
        "多倫多": 0
    },
    "學習地點": {
        "安省北部": 10,
        "GTA 外（不包北部）": 8,
        "GTA 內（唔包括多倫多）": 3,
        "多倫多": 0,
        "純網上完成": 0
    }
}

def main():
    root = tk.Tk()
    root.title("OINP 雇主擔保：國際學生打分器（粵語）")

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
