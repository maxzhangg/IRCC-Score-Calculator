import tkinter as tk
from tkinter import ttk, messagebox
import oinp_foreignworker_ZH_S
import oinp_indemandskill_ZH_S
import oinp_internationalstudent_ZH_S
import oinp_master_ZH_S
import oinp_phd_ZH_S

# 每个 stream 对应模块名
stream_modules = {
    "外国工人": "oinp_foreignworker_ZH_S",
    "紧缺技能": "oinp_indemandskill_ZH_S",
    "国际留学生": "oinp_internationalstudent_ZH_S",
    "硕士毕业生": "oinp_master_ZH_S",
    "博士毕业生": "oinp_phd_ZH_S"
}

def launch_gui():
    selected = stream_var.get()
    if not selected:
        messagebox.showwarning("请选择类别", "请选择一个 OINP 类别。")
        return

    module_name = stream_modules[selected]

    try:
        module = __import__(module_name)
        if hasattr(module, "main"):
            module.main()
        else:
            messagebox.showerror("函数缺失", f"{module_name}.py 文件中缺少 main() 函数。")
    except ModuleNotFoundError:
        messagebox.showerror("模块未找到", f"无法导入模块: {module_name}.py")
    except Exception as e:
        messagebox.showerror("错误", f"启动 {module_name}.py 失败\n\n{str(e)}")

# GUI 布局
root = tk.Tk()
root.title("OINP 打分器启动器（简体中文）")

frame = ttk.Frame(root, padding=20)
frame.grid()

ttk.Label(frame, text="请选择 OINP 类别:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
stream_var = tk.StringVar()
ttk.Combobox(frame, textvariable=stream_var, values=list(stream_modules.keys()), state="readonly", width=30).grid(row=0, column=1)

ttk.Button(frame, text="打开打分器", command=launch_gui).grid(row=1, column=0, columnspan=2, pady=20)

root.mainloop()
