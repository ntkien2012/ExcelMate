import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from excel_utils import read_excel_file

class ExcelReaderApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ExcelMate - File Reader")
        self.root.geometry("600x400")

        # Giao diện chính
        self.create_widgets()

    def create_widgets(self):
        # Nút chọn file
        self.open_button = tk.Button(self.root, text="Open Excel File", command=self.open_file)
        self.open_button.pack(pady=20)

        # Hiển thị dữ liệu
        self.text_box = tk.Text(self.root, wrap=tk.NONE, width=80, height=20)
        self.text_box.pack(padx=10, pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Excel Files", "*.xlsx *.xls")]
        )
        if not file_path:
            return

        try:
            data = read_excel_file(file_path)
            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(tk.END, data)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file: {e}")

    def run(self):
        self.root.mainloop()
