from tokenTypes import TokenKind
from split_str02 import get_tokens
from lexer import get_lexer


class DictNode:
  def __init__(self, key, value):
    self.key = key
    self.value = value


def set_value(value):
  pass


def set_key_value(key, value):
  pass


# 


def simple_parse(token_list):
  stack = None
  index = 0
  for _ in range(len(token_list)):
    itr = token_list[index]
    if index == 0 and (itr.kind == TokenKind.LBRACKET or
                       itr.kind == TokenKind.LBRACE):
      if itr.kind == TokenKind.LBRACKET:
        stack = list()
        index += 1
        continue
      if itr.kind == TokenKind.LBRACE:
        stack = dict()
        index += 1
        continue
      index += 1
    index
  return stack


def indent_deep(token_list):
  deep = 0
  stack = []
  for tkn in token_list:
    if tkn.kind == TokenKind.LBRACKET or tkn.kind == TokenKind.LBRACE:
      ele = {tkn.value: deep}
      stack.append(ele)
      tkn.deep = deep
      deep += 1
    if tkn.kind == TokenKind.RBRACE or tkn.kind == TokenKind.RBRACKET:
      deep -= 1
      ele = {tkn.value: deep}
      stack.append(ele)
      tkn.deep = deep

  pprint(stack)
  #return stack


def main():
  json_chr_list = list(json_data)
  pre_tokens = get_tokens(json_chr_list)
  json_tokens = get_lexer(pre_tokens)
  indent_deep(json_tokens)

  return json_tokens, simple_parse(json_tokens)


if __name__ == '__main__':
  from pprint import pprint
  from pathlib import Path

  json_path = Path('./sample01.json')
  json_data = json_path.read_text(encoding='utf-8')
  #json_data = '[{"nam e": "Taro", "age": 14, "check": true}, {"name": "Jiro", "age": 23, "check": false}, {"name": "Tom", "age": 16, "check": false}, {"name": null, "age": 14, "check": null}]'
  jjj, jptree = main()

