import json

json_data = '[{"nam e": "Taro", "age": 14, "check": true}, {"name": "Jiro", "age": 23, "check": false}, {"name": "Tom", "age": 16, "check": false}, {"name": null, "age": 14, "check": true}]'

json_chr_list = list(json_data)

j = json.loads(json_data)


# `"`
def pending_tokens(json_str):
  stack_bool = 0
  value = ''
  flag = 0
  tokens = []
  for chr in json_chr_list:
    if stack_bool:
      value += chr
    else:
      if chr == '[':
        tokens.append(chr)
        continue
      elif chr == '{':
        tokens.append(chr)
        continue
      elif chr == ':':
        tokens.append(chr)
        continue
      elif chr == ',':
        tokens.append(chr)
        continue
      elif chr == '}':
        tokens.append(chr)
        continue
      elif chr == ']':
        tokens.append(chr)
        continue

    if chr == '"':
      if stack_bool:
        tokens.append(value)
        value = ''
        stack_bool = 0
      else:
        value += chr
        stack_bool = 1
  return tokens


token_list = pending_tokens(json_chr_list)
print(len(json_chr_list))

for indx in range(len(json_chr_list)):
  if json_chr_list[indx] == 't':
    print(json_chr_list[indx: indx + 4])
  if json_chr_list[indx] == 'f':
    print(json_chr_list[indx: indx + 5])
  print(indx)

