'''
todo:
  - トークンとして分ける
  - 文字列は取れた
  - できれば`yield` で返したい
  
  - 文字列
  - 数値
  - bool
  - null
  
'''


def gen_strings(strings: str):
  str_obj = ''
  is_open = False
  pre_escape = False
  isin_string = False
  for char in strings:
    # 属性が何かを確認する

    if isin_string and is_open and pre_escape:
      str_obj += char
      is_open = True
      pre_escape = False
      continue

    if char == '"':
      isin_string = True
      if is_open:
        yield str_obj
        str_obj = ''
        isin_string = False
        is_open = False
      else:
        is_open = True
        continue

    if isin_string and is_open:
      str_obj += char
      if char == '\\':
        pre_escape = True
      continue

    if char in ['[', '{', ':', ',', '}', ']']:
      yield char


def set_string(char: str, str_obj: str, open_flag: bool, escape_flag: bool):
  if open_flag and escape_flag:
    str_obj += char
    open_flag = True
    escape_flag = False
    return str_obj, open_flag, escape_flag


def switch_flag(flag):
  pass


def division_strings(strings: str):
  obj_list = []
  token_obj = ''
  is_str = False
  in_escape = False
  is_number = False
  is_true = False
  is_false = False
  is_null = False

  for char in strings:
    # 属性が何かを確認する
    if not (is_str) and char.isspace():
      continue

    if is_str and in_escape:
      token_obj += char
      is_str = True
      in_escape = False
      continue

    if char == '"':
      if is_str:
        obj_list.append(token_obj)
        token_obj = ''
        is_str = False
        in_escape = False
        is_number = False
        is_true = False
        is_false = False
        is_null = False
      else:
        is_str = True
      continue

    if is_str:
      token_obj += char
      if char == '\\':
        in_escape = True
      continue

    if char in ['[', '{', ':', ',', '}', ']']:
      obj_list.append(char)
      #token_obj = ''
      is_str = False
      in_escape = False
      is_number = False
      is_true = False
      is_false = False
      is_null = False
      continue

    if not(is_str) and char == 't':
      is_true = True
      token_obj += char
      continue
      
    if not(is_str) and char == 'f':
      is_false = True
      token_obj += char
      continue
      
    if not(is_str) and char == 'n':
      is_null = True
      token_obj += char
      continue
      
    if is_true:
      token_obj += char
      if len(token_obj) >= 4:
        if token_obj == 'true':
          obj_list.append(token_obj)
          token_obj = ''
          is_str = False
          in_escape = False
          is_number = False
          is_true = False
          is_false = False
          is_null = False
          continue
        else:
          raise Exception(f'bool error: {token_obj}')
      continue
        
    if is_false:
      token_obj += char
      if len(token_obj) >= 5:
        if token_obj == 'false':
          obj_list.append(token_obj)
          token_obj = ''
          is_str = False
          in_escape = False
          is_number = False
          is_true = False
          is_false = False
          is_null = False
          continue
        else:
          raise Exception(f'bool error: {token_obj}')
      continue
      
    if is_null:
      token_obj += char
      if len(token_obj) >= 4:
        if token_obj == 'null':
          obj_list.append(token_obj)
          token_obj = ''
          is_str = False
          in_escape = False
          is_number = False
          is_true = False
          is_false = False
          is_null = False
          continue
        else:
          raise Exception(f'null error: {token_obj}')
      continue
    
      

  return obj_list


if __name__ == '__main__':
  from pathlib import Path
  import cProfile

  json_path = Path('./sample01.json')
  json_str = json_path.read_text(encoding='utf-8')
  json_list = division_strings(json_str)
  join_gen = gen_strings(json_str)
  join_gen_list = list(join_gen)
  print(join_gen_list == json_list)

  #cProfile.run('division_strings(json_str)', sort=1)
  #cProfile.run('gen_strings(json_str)', sort=1)

