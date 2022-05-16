def stack_str(string: str):
  is_escape = None


def division_strings(strings: str):
  div_list = []
  str_obj = ''
  is_open = False

  for char in strings:
    if char == '"':
      is_open = True
      continue
      
    if is_open and char == '"':
      print(str_obj)
      is_open = False
      str_obj = ''
      continue

    if is_open:
      str_obj += char


if __name__ == '__main__':
  from pathlib import Path
  import cProfile

  json_path = Path('./sample02.json')
  json_str = json_path.read_text(encoding='utf-8')
  json_list = division_strings(json_str)

