import pandas as pd

def read_excel_file(file_path):
    """
    Đọc nội dung từ file Excel và trả về chuỗi để hiển thị.
    """
    try:
        # Đọc file Excel
        df = pd.read_excel(file_path)
        return df.to_string(index=False)
    except Exception as e:
        raise RuntimeError(f"Error reading Excel file: {e}")
