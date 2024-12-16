## README for **ExcelMate**

### **Project Name:**  
**ExcelMate** - A Simple Excel File Reader

---

### **Description:**  
ExcelMate is a lightweight application designed to open and read Excel files (`.xlsx` and `.xls`) in a user-friendly graphical interface. It is built with Python, utilizing `tkinter` for the GUI and `pandas` for Excel file processing. This tool is perfect for users who need a quick way to view the content of Excel files without requiring a full-fledged spreadsheet editor.

---

### **Features:**  
- Open and display the contents of `.xlsx` and `.xls` files.  
- Easy-to-use graphical interface.  
- Lightweight and portable.  

---

### **Project Structure:**  

```
ExcelMate/
│
├── src/
│   ├── main.py          # Entry point of the application.
│   ├── gui.py           # Handles the graphical user interface.
│   ├── excel_utils.py   # Contains Excel file processing logic.
│
├── resources/           # Holds resources like icons and sample files.
│   ├── icon.ico         # Icon for the application (if any).
│
├── tests/               # Test cases for project functionality.
│   ├── test_excel_utils.py
│
├── requirements.txt     # List of dependencies.
├── README.md            # Documentation for the project.
└── .gitignore           # Git ignore file for excluding unnecessary files.
```

---

### **Installation:**  

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/ntkien2012/ExcelMate.git
   cd ExcelMate
   ```

2. **Set Up Virtual Environment (Optional but Recommended)**:  
   ```bash
   python -m venv env
   source env/bin/activate   # Linux/Mac
   env\Scripts\activate      # Windows
   ```

3. **Install Dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:  
   ```bash
   python src/main.py
   ```

---

### **Usage:**  

1. Launch the application by running `python src/main.py`.
2. Click on the "Open Excel File" button.
3. Select the `.xlsx` or `.xls` file you wish to view.
4. The content of the file will be displayed in a text box within the interface.

---

### **Dependencies:**  
- Python >= 3.8  
- `pandas`  
- `tkinter` (pre-installed with Python)  

---

### **Contributing:**  
Contributions are welcome! To contribute:  
1. Fork the repository.  
2. Create a feature branch:  
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes and push them to your fork.  
4. Open a pull request.

---

### **Known Issues:**  
- Large Excel files may take time to load.
- No support for editing or saving Excel files (view-only).

---

### **Future Improvements:**  
- Add support for editing and saving Excel files.  
- Display content in a table-like format using `ttk.Treeview`.  
- Support additional file formats (e.g., `.csv`).  

---

Enjoy using **ExcelMate**!