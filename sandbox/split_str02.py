json_data = '[{"nam e": "Taro", "age": 14, "check": true}, {"name": "Jiro", "age": 23, "check": false}, {"name": "Tom", "age": 16, "check": false}, {"name": null, "age": 14, "check": null}]'

json_chr_list = list(json_data)

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

