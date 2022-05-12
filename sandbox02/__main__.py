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
    self.key: bool = False
    self.nest: int = None
    self.indent: int = None

  def __str__(self):
    return str(self.value)


symbols = {
  '[': Token(TokenType.L_BRACKET, None),
  ']': Token(TokenType.R_BRACKET, None),
  '{': Token(TokenType.L_BRACE, None),
  '}': Token(TokenType.R_BRACE, None),
  ':': Token(TokenType.COLON, None),
  ':': Token(TokenType.COMMA, None),
}


def _switch_token(c: str, i: int) -> tuple:
  pass


def get_tokens(strs: str, index: int=0) -> list:
  char_list = list(strs)
  length = str_list.__len__()

  flag_symbols = ['[', ']', '{', '}', ':', ',']
  tokens = []
  _append = tokens.append
  for _ in range(length):
    if index >= length: break
    char = char_list[index]
    
    if char.isspace():
      index += 1
      continue


if __name__ == '__main__':
  from pathlib import Path

  json_path = Path('./sample02.json')
  json_str = json_path.read_text(encoding='utf-8')
  t = Token(TokenType.COLON, ':')

