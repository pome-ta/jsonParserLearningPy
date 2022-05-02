json_data = '''{
   "number":123,
   "boolean":true,
   "string":"togatoga",
   "object":{
      "number":2E10
   }
}
'''

json_data = '[{"nam e": "Taro", "age": 14, "check": true}, {"name": "Jiro", "age": 23, "check": false}, {"name": "Tom", "age": 16, "check": false}, {"name": null, "age": 14, "check": null}]'


def get_string_step(tail_list):
  quotation_flag = False
  for n, string in enumerate(tail_list):
    if string == '"':
      if quotation_flag:
        break
      if tail_list[n - 1] == '\\':
        continue
      quotation_flag = True
  str_value = ''.join(tail_list[:n + 1])
  return str_value, len(str_value)


def get_number_step(tail_list):
  end = [',', '}', ']', '\n']
  for n, number in enumerate(tail_list):
    if number in end:
      break
  num_value = ''.join(tail_list[:n])
  return num_value, len(num_value)


json_chr_list = list(json_data)
str_length = len(json_chr_list)
tokens = []
symbols = ['[', ']', '{', '}', ':', ',']
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
    # xxx: `true` 確認
    tokens.append(''.join(cut_top_list[:4]))
    index += 4
    continue

  if element == 'f':
    cut_top_list = json_chr_list[index:]
    # xxx: `false` 確認
    tokens.append(''.join(cut_top_list[:5]))
    index += 5
    continue

  if element == 'n':
    cut_top_list = json_chr_list[index:]
    # xxx: `null` 確認
    tokens.append(''.join(cut_top_list[:4]))
    index += 4
    continue

  # string
  if element == '"':
    cut_top_list = json_chr_list[index:]
    str_value, step = get_string_step(cut_top_list)
    tokens.append(str_value)
    index += step
    continue

  # number
  if element:
    cut_top_list = json_chr_list[index:]
    num_value, step = get_number_step(cut_top_list)
    tokens.append(num_value)
    index += step
    continue

  print(f'{element: element}')
  index += 1

