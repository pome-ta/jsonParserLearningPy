#import json

json_data = '[{"nam e": "Taro", "age": 14, "check": true}, {"name": "Jiro", "age": 23, "check": false}, {"name": "Tom", "age": 16, "check": false}, {"name": null, "age": 14, "check": null}]'

json_chr_list = list(json_data)

#j = json.loads(json_data)


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


#token_list = pending_tokens(json_chr_list)
#print(len(json_chr_list))
'''
for indx in range(len(json_chr_list)):
  if json_chr_list[indx] == 't':
    print(json_chr_list[indx: indx + 4])
  if json_chr_list[indx] == 'f':
    print(json_chr_list[indx: indx + 5])
  print(indx)

'''


def seek_quotation_index(crop_list):
  for n, string in enumerate(crop_list):
    if string == '"':
      if crop_list[n - 1] == '\\':
        continue
      return n


def seek_number_index(crop_list):
  n = crop_list.index(',')
  for n, string in enumerate(crop_list):
    if string == '"':
      if crop_list[n - 1] == '\\':
        continue
      return n


index = 0
str_length = len(json_chr_list)
quotation_flag = False
str_value = ''
tokens = []

symbols = ['[', ']', '{', '}', ':', ',']

for _ in range(str_length):
  if index >= str_length:
    break
  element = json_chr_list[index]
  

  if element in symbols:
    tokens.append(element)
    index += 1
    continue

  if element == 't':
    cut_top_list = json_chr_list[index:]
    tokens.append(''.join(cut_top_list[:4]))
    index += 4
    continue

  if element == 'f':
    cut_top_list = json_chr_list[index:]
    tokens.append(''.join(cut_top_list[:5]))
    index += 5
    continue
    
  if element == 'n':
    cut_top_list = json_chr_list[index:]
    tokens.append(''.join(cut_top_list[:4]))
    index += 4
    continue

  if element == '"':
    str_value += element
    index += 1
    cut_top_list = json_chr_list[index:]
    step_index = seek_quotation_index(cut_top_list) + 1
    str_value += ''.join(cut_top_list[:step_index])
    tokens.append(str_value)
    str_value = ''
    index += step_index
    continue

  index += 1

