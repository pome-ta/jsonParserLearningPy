from enum import Enum, auto
from typing import List

from tokenTypes import TokenKind
from split_str02 import get_tokens


class Token:
  def __init__(self, kind, value=None):
    self.kind = kind
    self.value = value

  def __eq__(self, other):
    if not isinstance(other, Token):
      return NotImplemented
    return self.kind == other.kind and self.value == other.value


'''
    def __str__(self):
      if self.kind == TokenKind.LBRACKET:
        return '['
      elif self.kind == TokenKind.LBRACE:
        return '{'
      elif self.kind == TokenKind.COLON:
        return ':'
      elif self.kind == TokenKind.COMMA:
        return ','
      elif self.kind == TokenKind.RBRACE:
        return '}'
      elif self.kind == TokenKind.RBRACKET:
        return ']'
      elif self.kind == TokenKind.STRING:
        return str(self.value)
      else:
        return str(self.value)

'''


# xxx: 2回回して無駄だけど取り敢えず
def get_lexer(token_list):
  stack = []
  for t in token_list:
    if t == '[':
      stack.append(Token(TokenKind.LBRACKET, t))
    elif t == '{':
      stack.append(Token(TokenKind.LBRACE, t))
    elif t == '{':
      stack.append(Token(TokenKind.LBRACE, t))
    elif t == ':':
      stack.append(Token(TokenKind.COLON, t))
    elif t == ',':
      stack.append(Token(TokenKind.COMMA, t))
    elif t == '}':
      stack.append(Token(TokenKind.RBRACE, t))
    elif t == ']':
      stack.append(Token(TokenKind.RBRACKET, t))
    elif t[0] == 't':
      stack.append(Token(TokenKind.BOOLEAN, t))
    elif t[0] == 'f':
      stack.append(Token(TokenKind.BOOLEAN, t))
    elif t[0] == 'n':
      stack.append(Token(TokenKind.NULL, t))
    elif t[0] == '"':
      value = t[1:len(t) - 1]
      stack.append(Token(TokenKind.STRING, value))
    else:
      stack.append(Token(TokenKind.NUMBER, t))

  return stack


if __name__ == '__main__':
  from pprint import pprint
  from pathlib import Path
  import json

  json_path = Path('./sample01.json')
  with open(json_path, encoding='utf-8') as f:
    mrj = json.load(f)
  json_data = json_path.read_text(encoding='utf-8')
  mlj = json.loads(json_data)
  json_chr_list = list(json_data)
  pre_tokens = get_tokens(json_chr_list)
  json_tokens = get_lexer(pre_tokens)

  for jt in json_tokens:
    print(f'{jt.kind} ->{jt.value}')

