json_data = '[{"nam e": "Taro", "age": 14, "check": true}, {"name": "Jiro", "age": 23, "check": false}, {"name": "Tom", "age": 16, "check": false}, {"name": null, "age": 14, "check": null}]'


def seek_quotation_index(crop_list):
  quotation_flag = False
  str_value = ''
  for n, string in enumerate(crop_list):
    if string == '"':
      if crop_list[n - 1] == '\\':
        continue
      return n


def seek_number_index(crop_list):
  num_value = ''
  n = crop_list.index(',')
  return n


json_chr_list = list(json_data)
str_length = len(json_chr_list)
tokens = []
symbols = ['[', ']', '{', '}', ':', ',']

str_value = ''
num_value = ''

index = 0

for _ in range(str_length):
  if index >= str_length:
    break
  element = json_chr_list[index]

  if element.isspace():
    index += 1
    continue

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

  # string
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

  # number
  if element:
    num_value += element
    index += 1
    cut_top_list = json_chr_list[index:]
    step_index = seek_number_index(cut_top_list)
    num_value += ''.join(cut_top_list[:step_index])
    tokens.append(num_value)
    num_value = ''
    index += step_index
    continue

  print(f'{element: element}')
  index += 1

