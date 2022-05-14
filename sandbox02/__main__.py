from enum import Enum, auto
from typing import Optional


class TokenType(Enum):
  NUMBER = auto()  # 数値
  STRING = auto()  # 文字列
  BOOLEAN = auto()  # true or false
  NULL = auto()  # null

  L_BRACKET = auto()  # [
  R_BRACKET = auto()  # ]
  L_BRACE = auto()  # {
  R_BRACE = auto()  # }
  COLON = auto()  # :
  COMMA = auto()  # ,


class Token:
  def __init__(self, token_type: TokenType, value: str = None):
    self.token_type: TokenType = token_type
    self.value: str = value
    self.obj_key: bool = False
    self.nest: Optional[int] = None
    self.indent: Optional[int] = None

  def __str__(self):
    return str(self.value)


# xxx: 無駄？
def _get_symbol_dict(value: str = None) -> dict:
  return {
    '[': Token(TokenType.L_BRACKET, value),
    ']': Token(TokenType.R_BRACKET, value),
    '{': Token(TokenType.L_BRACE, value),
    '}': Token(TokenType.R_BRACE, value),
    ':': Token(TokenType.COLON, value),
    ',': Token(TokenType.COMMA, value),
  }


bools2null_dict = {
  't': 'true',
  'f': 'false',
  'n': 'null',
}


def _get_strings_step(tail_list: list) -> tuple:
  quotation_flag = False
  for n, string in enumerate(tail_list):
    if string == '"':
      if n and tail_list[n - 1] == '\\':
        continue
      if quotation_flag:
        break
      quotation_flag = True
  str_list = tail_list[:n + 1]
  str_value = ''.join(str_list[1:n])    # xxx: エスケープやら文字エンコードなど
  return Token(TokenType.STRING, str_value), len(str_list)


def _get_numbers_step(tail_list: list) -> tuple:
  end = [',', '}', ']', '\n']  # xxx: `10,000` みたいな表現できない
  for n, number in enumerate(tail_list):
    if number in end:
      break
  num_value = ''.join(tail_list[:n])
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


def get_tokens(strs: str) -> list:
  char_list = list(strs)
  length = char_list.__len__()
  tokens = []

  flag_symbols = _get_symbol_dict().keys()
  flag_bool2null = bools2null_dict.keys()
  flag_numbers = [*(lambda: [str(n) for n in range(10)])(), '.', '-', 'e', 'E']   # xxx: `e`, `E` は不要？

  index = 0
  for _ in range(length):
    if index >= length:
      break
    char = char_list[index]

    if char.isspace():
      index += 1
      continue  # 空白は早々に棄却

    if char in flag_symbols:
      tkn = _get_symbol_dict(char)[char]
      add_index = 1
    elif char in flag_bool2null:
      tkn, add_index = _get_bools2null_step(
        char_list[index:index + 5 if char == 'f' else index + 4])
    elif char == '"':
      tkn, add_index = _get_strings_step(char_list[index:])
    elif char in flag_numbers:
      tkn, add_index = _get_numbers_step(char_list[index:])

    else:  # xxx: エラー処理
      raise Exception(f'Token error: {char}')
    index += add_index
    tokens.append(tkn)
  return tokens


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

  if nest_num != 1:  # xxx: エラー処理
    raise Exception('nest error: nest panic')


def _get_index2indent_dict(tokens: list) -> list:
  index_indent_list = []
  for index, tkn in enumerate(tokens):
    if tkn.nest:
      index_indent_list.append({'index': index, 'indent': tkn.nest})
  return index_indent_list


def _get_nest2indent_list(tokens: list) -> list:
  nest_indent_list = []   # xxx: `index` と、`indent` が紛らわしい？

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

  if len(set(pool + ref)) != 1:
    raise Exception('indent error: indent panic')
  return nest_indent_list


def _set_indent(tokens: list, nests: list) -> None:
  for o, c, i in nests:
    ext_tokens = tokens[o:c + 1]
    for tkn in ext_tokens:
      tkn.indent = i


def parse(strs: str):
  token_list = get_tokens(strs)
  _set_attributes(token_list)
  nest_indent_list = _get_nest2indent_list(token_list)
  _set_indent(token_list, nest_indent_list)
  return token_list


if __name__ == '__main__':
  from pathlib import Path

  json_path = Path('./sample02.json')
  json_str = json_path.read_text(encoding='utf-8')
  t = Token(TokenType.COLON, ':')
  main = parse(json_str)
