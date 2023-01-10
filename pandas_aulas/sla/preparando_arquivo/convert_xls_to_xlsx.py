import os

filename = 'rel_sla_teste.xls'
os.system(f'libreoffice --convert-to xlsx {filename} --headless')

