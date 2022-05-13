from enum import Enum, auto


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
  def __init__(self, type, value=None):
    self.type: TokenType = type
    self.value: str = value
    self.obj_key: bool = False
    self.nest: int = None
    self.indent: int = None

  def __str__(self):
    return str(self.value)


# xxx: 無駄？
def _get_symbol_dict(value: str=None) -> dict:
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
      if n and tail_list[n - 1] == '\\': continue
      if quotation_flag: break
      quotation_flag = True
  str_list = tail_list[:n + 1]
  # xxx: エスケープやら文字エンコードなど
  str_value = ''.join(str_list[1:n])
  return Token(TokenType.STRING, str_value), len(str_list)


def _get_numbers_step(tail_list: list) -> tuple:
  # xxx: `10,000` みたいな表現できない
  end = [',', '}', ']', '\n']
  for n, number in enumerate(tail_list):
    if number in end: break
  num_value = ''.join(tail_list[:n])
  return Token(TokenType.NUMBER, num_value), len(num_value)


def _get_bools2null_step(value_list: list) -> tuple:
  bool_null = ''.join(value_list)
  if bool_null == bools2null_dict[value_list[0]]:
    # xxx 長すぎー？
    tkn = Token(TokenType.NULL, bool_null) if bool_null == 'null' else Token(
      TokenType.BOOLEAN, bool_null)

  else:
    raise Exception(f'bool or null typeError: {bool_null}')
  return tkn, len(bool_null)


def get_tokens(strs: str) -> list:
  char_list = list(strs)
  length = char_list.__len__()
  tokens = []

  flag_symbols = _get_symbol_dict().keys()
  flag_bool2null = bools2null_dict.keys()
  # xxx: `e`, `E` は不要？
  flag_numbers = [*(lambda: [str(n) for n in range(10)])(), '.', '-', 'e', 'E']

  index = 0
  for _ in range(length):
    if index >= length: break
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
    # xxx: エラー処理
    else:
      raise Exception
    index += add_index
    tokens.append(tkn)
  return tokens





def parse(strs: str):
  token_list = get_tokens(strs)
  return token_list


if __name__ == '__main__':
  from pathlib import Path

  json_path = Path('./sample02.json')
  json_str = json_path.read_text(encoding='utf-8')
  t = Token(TokenType.COLON, ':')
  main = get_tokens(json_str)

