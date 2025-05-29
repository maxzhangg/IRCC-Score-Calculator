import tkinter as tk
from tkinter import ttk

# 粵語打分規則
scoring_rules_yue_phd = {
    "工作/學習簽證狀態": {
        "持有有效工作/學習簽證": 10,
        "冇有效簽證": 0
    },
    "收入歷史（過去5年稅單）": {
        "單一年收入 ≥ $40,000": 3,
        "單一年收入 < $40,000": 0
    },
    "最高學歷": {
        "博士（PhD）": 10,
        "碩士": 8,
        "學士或等同": 6,
        "研究生文憑/證書": 6,
        "大專文憑/證書": 5,
        "學徒或技術證書": 5,
        "少於大專水平": 0
    },
    "學習領域": {
        "STEM / 醫療 / 工程 / 精密生產 / 建築等": 12,
        "商業 / 法律 / 教育 / 社工 / 交通等": 6,
        "文科 / 人文 / BHASE 等其他": 0
    },
    "加拿大学歷經驗": {
        "多於一個學歷": 10,
        "只有一個學歷": 5
    },
    "官方語言能力（CLB）": {
        "CLB 9 或以上": 10,
        "CLB 8": 6,
        "CLB 7": 4,
        "CLB 6 或以下": 0
    },
    "官方語言數量": {
        "識兩種語言（CLB 7+ 同 CLB 6+）": 10,
        "識一種語言": 5
    },
    "地區（學習地點）": {
        "安省北部": 10,
        "GTA 以外地區（唔包括北部）": 8,
        "GTA（唔包括多倫多）": 3,
        "多倫多": 0,
        "冇親身上堂": 0
    }
}

def main():
    root = tk.Tk()
    root.title("OINP 博士畢業生類別打分器（粵語）")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")

    variables = {}
    row = 0

    for category, options in scoring_rules_yue_phd.items():
        ttk.Label(frame, text=category).grid(row=row, column=0, sticky="w", pady=5)
        var = tk.StringVar()
        variables[category] = var
        combo = ttk.Combobox(frame, textvariable=var, values=list(options.keys()), state="readonly", width=60)
        combo.grid(row=row, column=1, pady=5)
        row += 1

    result_var = tk.StringVar(value="總分: 0")
    ttk.Label(frame, textvariable=result_var, font=("Arial", 12, "bold")).grid(row=row, columnspan=2, pady=10)

    def calculate_score():
        total = 0
        for cat, var in variables.items():
            choice = var.get()
            if choice in scoring_rules_yue_phd[cat]:
                total += scoring_rules_yue_phd[cat][choice]
        result_var.set(f"總分: {total}")

    ttk.Button(frame, text="計算總分", command=calculate_score).grid(row=row+1, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
