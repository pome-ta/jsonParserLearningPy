from enum import Enum, auto
from typing import List

from tokenTypes 
from split_str02 import get_tokens



class Token:
  def __init__(self, kind, value=None):
    self.kind = kind
    self.value = value

  def __eq__(self, other):
    if not isinstance(other, Token):
      return NotImplemented
    return self.kind == other.kind and self.value == other.value
    
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
        return f'{self.value}'
      else:
        return str(self.value)

def get_lexer(token_list):
  stack = []
  for t in token_list:
    if t == '[':
      stack.append()
      
      

if __name__ == '__main__':
  from pprint import pprint
  from pathlib import Path
  tokens = []
  json_path = Path('./sample01.json')
  json_data = json_path.read_text(encoding='utf-8')
  json_chr_list = list(json_data)
  json_tokens = get_tokens(json_chr_list)
  

