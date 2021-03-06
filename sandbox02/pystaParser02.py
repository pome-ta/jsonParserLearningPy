import re
from enum import Enum  # , auto
from typing import Optional

__all__ = ['parse', 'get_tokens']


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


bools2null_dict = {
  't': 'true',
  'f': 'false',
  'n': 'null',
}


def _get_strings_step(tail_list: list) -> tuple:
  index = 0
  quotation_flag = False
  for n, string in enumerate(tail_list):
    index = n
    if string == '"':
      if n and tail_list[n - 1] == '\\':
        continue
      if quotation_flag:
        break
      quotation_flag = True
  str_list = tail_list[:index + 1]
  str_value = ''.join(str_list[1:index])  # xxx: エスケープやら文字エンコードなど
  return Token(TokenType.STRING, str_value), len(str_list)


def _get_numbers_step(tail_list: list) -> tuple:
  end = [',', '}', ']', '\n']  # xxx: `10,000` みたいな表現できない
  index = 0
  for n, number in enumerate(tail_list):
    index = n
    if number in end:
      break
  num_value = ''.join(tail_list[:index])
  return Token(TokenType.NUMBER, num_value), len(num_value)


def _get_bools2null_step(value_list: list) -> tuple:
  bool_null = ''.join(value_list)
  if bool_null == bools2null_dict[value_list[0]]:
    # xxx 長すぎー？
    tkn = Token(TokenType.NULL, bool_null) if bool_null == 'null' else Token(
      TokenType.BOOLEAN, bool_null)

  else:  # xxx: エラー処理
    raise Exception(f'bool or null typeError: {bool_null}')
  return tkn, len(bool_null)


def get_tokens(strs: str) -> list:  # xxx: 長いな
  char_list = list(strs)
  length = char_list.__len__()
  tokens = []

  match_symbols = ['[', ']', '{', '}', ':', ',']
  match_bool2null = bools2null_dict.keys()
  match_numbers = [
    *(lambda: [str(n) for n in range(10)])(), '.', '-', 'e', 'E'
  ]  # xxx: `e`, `E` は不要？
  nest = 1  # xxx `if` 処理の`Falsy(0)` 回避のため
  index = 0
  for _ in range(length):
    if index >= length:
      break
    char = char_list[index]

    if char.isspace():
      index += 1
      continue  # 空白は早々に棄却

    if char in match_symbols:
      tkn = _switch_symbol_token(char)
      if tkn.token_type in [
          TokenType.L_BRACE, TokenType.L_BRACKET, TokenType.R_BRACE,
          TokenType.R_BRACKET
      ]:
        nest = _setup_nest(tkn, nest)
      if tkn.token_type == TokenType.COLON:
        try:
          tokens[-1].obj_key = True
        except Exception as e:
          print(f'error: {e}')
      add_index = 1
    elif char in match_bool2null:
      tkn, add_index = _get_bools2null_step(
        char_list[index:index + 5 if char == 'f' else index + 4])
    elif char == '"':
      tkn, add_index = _get_strings_step(char_list[index:])
    elif char in match_numbers:
      tkn, add_index = _get_numbers_step(char_list[index:])

    else:  # xxx: エラー処理
      raise Exception(f'Token error: {char}')
    index += add_index
    end_flag = False if tkn.token_type in [
      TokenType.R_BRACE, TokenType.R_BRACKET
    ] else True
    tkn.indent = nest - end_flag
    tokens.append(tkn)

  if nest != 1:  # xxx: エラー処理
    raise Exception('nest error: nest panic')

  return tokens


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






def _setup_nest(tkn: Token, nest: int) -> int:
  if tkn.token_type in [TokenType.L_BRACE, TokenType.L_BRACKET]:
    tkn.nest = nest
    nest += 1
  if tkn.token_type in [TokenType.R_BRACE, TokenType.R_BRACKET]:
    nest -= 1
    tkn.nest = nest
  return nest


def _setup_objkey(f_tkn: Token, s_tkn: Token) -> None:
  if s_tkn and s_tkn.token_type == TokenType.COLON:
    f_tkn.obj_key = True


def _set_attributes(tokens) -> None:
  length = tokens.__len__()
  nest_num = 1  # xxx `if` 処理の`Falsy(0)` 回避のため
  for index in range(length):
    now_tkn = tokens[index]
    nest_num = _setup_nest(now_tkn, nest_num)
    next_tkn = tokens[index + 1] if index + 1 < length else None
    _setup_objkey(now_tkn, next_tkn)


def _get_index2indent_dict(tokens: list) -> list:
  index_indent_list = []
  for index, tkn in enumerate(tokens):
    if tkn.nest:
      index_indent_list.append({'index': index, 'indent': tkn.nest})
  return index_indent_list


def _get_nest2indent_list(tokens: list) -> list:
  nest_indent_list = []  # xxx: `index` と、`indent` が紛らわしい？
  pool = _get_index2indent_dict(tokens)
  ref = [p for p in pool]

  length = pool.__len__()
  for open_index in range(length):
    open_nest = pool[open_index]
    if open_nest is None:
      continue
    indent_num = pool[open_index]['indent']
    pool[open_index] = None
    ref[open_index] = None

    for close_index in range(length):
      close_nest = ref[close_index]

      if close_nest and open_nest['indent'] == close_nest['indent']:
        nest_indent_list.append(
          [open_nest['index'], close_nest['index'], indent_num])
        ref[close_index] = None
        pool[close_index] = None
        break

  if len(set(pool + ref)) != 1:  # xxx: エラー処理
    raise Exception('indent error: indent panic')
  return nest_indent_list


def _set_indent(tokens: list, nests: list) -> None:
  for o, c, i in nests:
    ext_tokens = tokens[o:c + 1]
    for tkn in ext_tokens:
      tkn.indent = i


def _convert_value(tkn: Token) -> Optional:  # xxx: type
  if tkn.token_type == TokenType.BOOLEAN:
    value = True if re.search(r't', tkn.value) else False
  elif tkn.token_type == TokenType.NULL:
    value = None
  elif tkn.token_type == TokenType.NUMBER:
    value = float(tkn.value) if re.search(r'[.|eE]',
                                          tkn.value) else int(tkn.value)
  else:
    value = str(tkn.value)
  return value


def _get_dicts(tokens: list, indent: int) -> dict:
  dic_key = None
  dic_value = None
  values = []
  dicts = {}
  colon_flag = False
  children_flag = False
  for tkn in tokens:
    if tkn.indent == indent:
      dic_key = tkn.value if tkn.obj_key else dic_key

      colon_flag = True if tkn.token_type == TokenType.COLON else colon_flag

      if tkn.token_type in [TokenType.COMMA, TokenType.R_BRACE]:
        if children_flag:
          children_flag = False
          dic_value = _get_json_obj(values, indent + 1)

        dicts.update({dic_key: dic_value})
        dic_key = None
        dic_value = None
        values = []
      if colon_flag and not (
          tkn.token_type in [TokenType.COMMA, TokenType.COLON]):
        dic_value = _convert_value(tkn)

    else:
      values.append(tkn)
      children_flag = True
  return dicts


def _get_arrays(tokens: list, indent: int) -> list:
  array_value = None
  values = []
  arrays = []
  children_flag = False
  for tkn in tokens:
    if tkn.indent == indent:
      if tkn.token_type in [TokenType.COMMA, TokenType.R_BRACKET]:
        if children_flag:
          children_flag = False
          array_value = _get_json_obj(values, indent + 1)
        arrays.append(array_value)
        array_value = None
        values = []
      if not (tkn.token_type in [TokenType.L_BRACKET, TokenType.COMMA]):
        array_value = _convert_value(tkn)
    else:
      values.append(tkn)
      children_flag = True
  return arrays


def _get_json_obj(tokens: list, indent: int=1) -> dict:
  objs = None  # memo: 再帰呼び出し開始
  if tokens[0].token_type == TokenType.L_BRACKET:
    objs = _get_arrays(tokens, indent)
  elif tokens[0].token_type == TokenType.L_BRACE:
    objs = _get_dicts(tokens, indent)
  return objs


def parse(strs: str):
  #token_list = get_tokens(strs)
  token_list = division_strings(strs)
  
  _set_attributes(token_list)
  nest_indent_list = _get_nest2indent_list(token_list)
  _set_indent(token_list, nest_indent_list)
  json_objs = _get_json_obj(token_list)
  return json_objs, token_list


if __name__ == '__main__':
  from pathlib import Path
  import json

  json_path = Path('./sample04.json')
  json_str = json_path.read_text(encoding='utf-8')

  main_json, main_token = parse(json_str)
  main_char = list(json_str)
  main_sample = json.loads(json_str)
  print(main_json == main_sample)


