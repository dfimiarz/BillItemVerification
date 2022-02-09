import pandas
import os

def runscript():
    # Main function
    env = os.environ.get("PYTHON_ENV", default="development")
    filename = os.environ.get("FILE", default="BillItems.xlsx")
    worksheetname = os.environ.get("WORKSHEET", default="BillItems")
    excel_data_frame = pandas.read_excel(filename,sheet_name=worksheetname)

    print(excel_data_frame)

if __name__ == '__main__':
    runscript();
