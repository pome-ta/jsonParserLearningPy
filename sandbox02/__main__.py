from pathlib import Path

file_path = Path('./sample02.json')
str_data = file_path.read_text(encoding='utf-8')

a_s = '-1.1'
try:
  a_n = int(a_s)
except Exception as e:
  a_n = float(a_s)

aaa = 100
