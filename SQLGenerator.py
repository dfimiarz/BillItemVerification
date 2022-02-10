from cmath import isnan
from numpy import dtype, int32
import pandas
import numpy as np
import os
import math


excel_dtypes = {'id':pandas.Int32Dtype(),'invoice':pandas.Int32Dtype(),'pi':pandas.Int32Dtype(),\
'details':pandas.StringDtype(),'service_id':pandas.Int32Dtype(),'name':pandas.StringDtype(),\
'notes':pandas.StringDtype(),'log_details':pandas.pandas.StringDtype(),\
'log_notes': pandas.StringDtype(),'checked':pandas.BooleanDtype()}

excel_converters = {'service_start_time':pandas.to_datetime,'service_end_time':pandas.to_datetime,'log_start_time':pandas.to_datetime,'log_end_time':pandas.to_datetime}

def runscript():
    # Main function
    env = os.environ.get("PYTHON_ENV", default="development")
    filename = os.environ.get("FILE", default="BillItems.xlsx")
    worksheetname = os.environ.get("WORKSHEET", default="BillItems")
    excel_data_frame = pandas.read_excel(filename,sheet_name=worksheetname,dtype=excel_dtypes,converters=excel_converters)

    print(excel_data_frame.dtypes)



if __name__ == '__main__':
    runscript();
