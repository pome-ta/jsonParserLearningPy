from enum import Enum  # , auto

class TokenType(Enum):
  NUMBER = 1  # auto()  # 数値
  STRING = 2  # auto()  # 文字列
  BOOLEAN = 3  # auto()  # true or false
  NULL = 4  # auto()  # null

  L_BRACKET = 5  # auto()  # [
  R_BRACKET = 6  # auto()  # ]
  L_BRACE = 7  # auto()  # {
  R_BRACE = 8  # auto()  # }
  COLON = 9  # auto()  # :
  COMMA = 10  # auto()  # ,


class Token:
  def __init__(self, token_type: TokenType, value: str=None):
    self.token_type: TokenType = token_type
    self.value: str = value
    self.obj_key: bool = False
    self.nest: Optional[int] = None
    self.indent: Optional[int] = None

  def __str__(self):
    return str(self.value)


def _switch_symbol_token(value: str) -> Token:
  if value == '[':
    tkn = Token(TokenType.L_BRACKET, value)
  elif value == ']':
    tkn = Token(TokenType.R_BRACKET, value)
  elif value == '{':
    tkn = Token(TokenType.L_BRACE, value)
  elif value == '}':
    tkn = Token(TokenType.R_BRACE, value)
  elif value == ':':
    tkn = Token(TokenType.COLON, value)
  elif value == ',':
    tkn = Token(TokenType.COMMA, value)
  else:
    raise Exception(f'symbol typeError: {value}')
  return tkn



def division_strings(strings: str):
  match_numbers = [
    *(lambda: [str(n) for n in range(10)])(), '.', '-', 'e', 'E'
  ]  # xxx: `e`, `E` は不要？
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

    #print(char)
    if is_str and in_escape:
      token_obj += char
      is_str = True
      in_escape = False
      continue

    if char == '"':
      if is_str:
        obj_list.append(Token(TokenType.STRING, token_obj))
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
      if token_obj:  # todo is_number
        #print(is_str, in_escape, is_number, is_true, is_false, is_null)
        obj_list.append(Token(TokenType.NUMBER, token_obj))
      obj_list.append(_switch_symbol_token(char))
      token_obj = ''
      is_str = False
      in_escape = False
      is_number = False
      is_true = False
      is_false = False
      is_null = False
      continue

    if not (is_str) and char == 't':
      is_true = True
      token_obj += char
      continue

    if not (is_str) and char == 'f':
      is_false = True
      token_obj += char
      continue

    if not (is_str) and char == 'n':
      is_null = True
      token_obj += char
      continue

    if is_true:
      token_obj += char
      if len(token_obj) >= 4:
        if token_obj == 'true':
          obj_list.append(Token(TokenType.BOOLEAN, token_obj))
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
          obj_list.append(Token(TokenType.BOOLEAN, token_obj))
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
          obj_list.append(Token(TokenType.NULL, token_obj))
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

    if not (is_number) and char in match_numbers:
      is_number = True
      token_obj += char
      continue

    if is_number:
      token_obj += char
      continue

  return obj_list


if __name__ == '__main__':
  from pathlib import Path
  import cProfile

  json_path = Path('./sample04.json')
  json_str = json_path.read_text(encoding='utf-8')
  
  #json_list = division_strings(json_str)
  

  cProfile.run('division_strings(json_str)', sort=1)
  

