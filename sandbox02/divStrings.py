def gen_strings(strings: str):
  str_obj = ''
  is_open = False
  pre_escape = False
  for char in strings:
    if is_open and pre_escape:
      str_obj += char
      is_open = True
      pre_escape = False
      continue

    if char == '"':
      #str_obj += char

      if is_open:
        #str_list.append(''.join(str_obj[1:-1]))
        yield str_obj
        str_obj = ''
        is_open = False
      else:
        is_open = True
        continue

    if is_open:
      str_obj += char
      if char == '\\':
        pre_escape = True


def division_strings(strings: str):
  str_list = []
  str_obj = ''
  is_open = False
  pre_escape = False

  for char in strings:
    if is_open and pre_escape:
      str_obj += char
      is_open = True
      pre_escape = False
      continue

    if char == '"':
      #str_obj += char

      if is_open:
        str_list.append(str_obj)
        str_obj = ''
        is_open = False
      else:
        is_open = True
        continue

    if is_open:
      str_obj += char
      if char == '\\':
        pre_escape = True

  return str_list


if __name__ == '__main__':
  from pathlib import Path
  import cProfile

  json_path = Path('./sample01.json')
  json_str = json_path.read_text(encoding='utf-8')
  json_list = division_strings(json_str)
  join_gen = gen_strings(json_str)
  print(list(join_gen))
  #cProfile.run('division_strings(json_str)', sort=1)

