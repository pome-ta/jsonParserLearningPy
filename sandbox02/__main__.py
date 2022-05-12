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


# xxx: 無駄？
def _get_symbol_dict()->dict:
  return {
    '[': Token(TokenType.L_BRACKET, None),
    ']': Token(TokenType.R_BRACKET, None),
    '{': Token(TokenType.L_BRACE, None),
    '}': Token(TokenType.R_BRACE, None),
    ':': Token(TokenType.COLON, None),
    ',': Token(TokenType.COMMA, None),
  }



def _get_bool2null_dict()->dict:
  return {
    't': Token(TokenType.BOOLEAN, None),
    'f': Token(TokenType.BOOLEAN, None),
    'n': Token(TokenType.NULL, None),
  }


flag_symbols = _get_symbol_dict().keys()
flag_bool2null = _get_bool2null_dict().keys()


def _switch_token(c: str, i: int) -> tuple:
  tkn, tail = [None, None]
  if c.isspace():
    return tkn, i + 1, tail
  if c in flag_symbols:
    tkn = _get_symbol_dict()[c]
    return tkn, i + 1, tail
  if c in flag_bool2null:
    tkn = _get_bool2null_dict()[c]
    

def _check_bool2null(v: str):
  pass


def get_tokens(strs: str, index: int=0) -> list:
  char_list = list(strs)
  length = char_list.__len__()
  tokens = []
  _append = tokens.append
  for _ in range(length):
    if index >= length: break
    tkn, next_index, tail = _switch_token(char_list[index], index)
    if tkn:
      value = char_list[index:tail] if tail else char_list[index]
      
      tkn.value = value
      _append(tkn)
    index = next_index
  return tokens


if __name__ == '__main__':
  from pathlib import Path

  json_path = Path('./sample03.json')
  json_str = json_path.read_text(encoding='utf-8')
  t = Token(TokenType.COLON, ':')
  main = get_tokens(json_str)

