from enum import Enum, auto


class TokenKind(Enum):
  # リテラル
  NUMBER = auto()  # 数値
  STRING = auto()  # 文字列
  BOOLEAN = auto()  # true または false
  NULL = auto()  # null

  # 記号
  LBRACKET = auto()  # [
  LBRACE = auto()  # {
  COLON = auto()  # :
  COMMA = auto()  # ,
  RBRACE = auto()  # }
  RBRACKET = auto()  # ]


if __name__ == '__main__':
  for token in TokenKind:
    #print(token)
    pass
  comma = TokenKind(8)
  print(comma)

