import os
import pandas as pd


df_list = []

for filetest in sorted(os.listdir()):
    if filetest.endswith('txt') and not filetest == 'file_full.txt':
        df_list.append(pd.read_csv(filetest, skiprows=6))

concat_df = pd.concat(df_list)
excel_file = concat_df.to_excel('file_full.xlsx')
