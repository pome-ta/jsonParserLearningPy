def stack_str(string: str):
  is_escape = None


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
      str_obj += char
      if is_open:
        str_list.append(''.join(str_obj[1:-1]))
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

  json_path = Path('./sample04.json')
  json_str = json_path.read_text(encoding='utf-8')
  #json_list = division_strings(json_str)
  cProfile.run('division_strings(json_str)', sort=1)

