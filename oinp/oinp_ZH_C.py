import tkinter as tk
from tkinter import ttk, messagebox

# 每個 stream 對應模組名稱（繁體中文）
stream_modules = {
    "外國工人（Foreign Worker）": "oinp_foreignworker_ZH_C",
    "需求技能（In-Demand Skills）": "oinp_indemandskill_ZH_C",
    "國際學生（International Student）": "oinp_internationalstudent_ZH_C",
    "碩士畢業生（Master Graduate）": "oinp_master_ZH_C",
    "博士畢業生（PhD Graduate）": "oinp_phd_ZH_C"
}

def launch_gui():
    selected = stream_var.get()
    if not selected:
        messagebox.showwarning("未選擇項目", "請選擇一個申請類別。")
        return

    module_name = stream_modules[selected]

    try:
        module = __import__(module_name)
        if hasattr(module, "main"):
            module.main()
        else:
            messagebox.showerror("缺少主函式", f"{module_name}.py 沒有 main() 函式。")
    except ModuleNotFoundError:
        messagebox.showerror("模組未找到", f"無法匯入模組：{module_name}.py")
    except Exception as e:
        messagebox.showerror("錯誤", f"啟動 {module_name}.py 失敗。\n\n{str(e)}")

# GUI 佈局
root = tk.Tk()
root.title("OINP 評分工具啟動器（繁體中文）")

frame = ttk.Frame(root, padding=20)
frame.grid()

ttk.Label(frame, text="請選擇 OINP 申請類別：").grid(row=0, column=0, padx=10, pady=10, sticky="e")
stream_var = tk.StringVar()
ttk.Combobox(frame, textvariable=stream_var, values=list(stream_modules.keys()), state="readonly", width=35).grid(row=0, column=1)

ttk.Button(frame, text="開始評分", command=launch_gui).grid(row=1, column=0, columnspan=2, pady=20)

root.mainloop()
