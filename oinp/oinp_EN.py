import tkinter as tk
from tkinter import ttk, messagebox

# 每个 stream 对应模块名
stream_modules = {
    "Foreign Worker": "oinp_foreignworker_EN",
    "In-Demand Skills": "oinp_indemandskill_EN",
    "International Student": "oinp_internationalstudent_EN",
    "Master Graduate": "oinp_master_EN",
    "PhD Graduate": "oinp_phd_EN"
}

def launch_gui():
    selected = stream_var.get()
    if not selected:
        messagebox.showwarning("Selection missing", "Please select a stream.")
        return

    module_name = stream_modules[selected]

    try:
        module = __import__(module_name)
        if hasattr(module, "main"):
            module.main()
        else:
            messagebox.showerror("Missing Function", f"{module_name}.py does not have a main() function.")
    except ModuleNotFoundError:
        messagebox.showerror("Module Not Found", f"Cannot import module: {module_name}.py")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to launch {module_name}.py\n\n{str(e)}")

# GUI Layout
root = tk.Tk()
root.title("OINP Scoring Tool Launcher (English)")

frame = ttk.Frame(root, padding=20)
frame.grid()

ttk.Label(frame, text="Select OINP Stream:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
stream_var = tk.StringVar()
ttk.Combobox(frame, textvariable=stream_var, values=list(stream_modules.keys()), state="readonly", width=30).grid(row=0, column=1)

ttk.Button(frame, text="Launch", command=launch_gui).grid(row=1, column=0, columnspan=2, pady=20)

root.mainloop()
