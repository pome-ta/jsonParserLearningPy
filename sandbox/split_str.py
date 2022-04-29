json_data = '[{"nam e": "Taro", "age": 14, "check": true}, {"name": "Jiro", "age": 23, "check": false}, {"name": "Tom", "age": 16, "check": false}]'

json_chr_list = list(json_data)

stack_bool = 0
value = ''
flag = 0
token = []


# `"`

for chr in json_chr_list:
  
  if chr == '"':
    value += chr
