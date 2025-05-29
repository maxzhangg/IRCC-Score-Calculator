# OINP Scoring Tool (GUI)

A lightweight GUI application to help candidates calculate their scores for the Ontario Immigrant Nominee Program (OINP), supporting five major streams. This repository includes English, Simplified Chinese, and Traditional Chinese versions of the launcher.

---

## 🔍 Supported OINP Streams

- Foreign Worker
- In-Demand Skills
- International Student
- Master Graduate
- PhD Graduate

Each stream has its own score calculator, implemented in modular Python files with a unified launcher interface.

---

## 🖥️ Features

- Select stream from dropdown menu
- Launch independent scoring interface per stream
- English, 简体中文, 繁體中文 versions available
- One-click `.exe` build via `PyInstaller` (no installer required)

---

## 📂 Project Structure

```
oinp/
├── oinp_EN.py           # English launcher
├── oinp_ZH_S.py         # 简体中文版启动器
├── oinp_ZH_C.py         # 繁體中文版啟動器
├── oinp_foreignworker_EN.py
├── oinp_foreignworker_ZH_S.py
├── oinp_foreignworker_ZH_C.py
└── ... (other stream modules)

```

---

## 🚀 How to Run

### Option 1: Run via Python

```bash
python oinp_EN.py        # English
python oinp_ZH_S.py      # 简体中文
python oinp_ZH_C.py      # 繁體中文
```

> Python 3.6+ and Tkinter required.

### Option 2: Build Executable (no Python required)

Using [PyInstaller](https://pyinstaller.org/):

```bash
pyinstaller --noconfirm --onefile oinp_EN.py
pyinstaller --noconfirm --onefile oinp_ZH_S.py
pyinstaller --noconfirm --onefile oinp_ZH_C.py
```

---

## 📦 Dependencies

Only standard library used:

```txt
tk
```

---

## 📌 Notes

- Each submodule (e.g. `oinp_foreignworker_EN.py`) must define a `main()` function to launch its GUI.
- This is a launcher script that dynamically imports and runs the correct module based on user selection.

---

## 📄 License

MIT License
