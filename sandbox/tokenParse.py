from tokenTypes import TokenKind
from split_str02 import get_tokens
from lexer import get_lexer


def simple_parse(token_list):
  stack = None
  for index in range(len(token_list)):
    if index == 0 and (token_list[index].kind == TokenKind.LBRACKET or
                       token_list[index].kind == TokenKind.LBRACE):
      if token_list[index].kind == TokenKind.LBRACKET:
        stack = list()
        continue
      if token_list[index].kind == TokenKind.LBRACE:
        stack = dict()
        continue
    index


def main():
  json_chr_list = list(json_data)
  pre_tokens = get_tokens(json_chr_list)
  json_tokens = get_lexer(pre_tokens)
  simple_parse(json_tokens)
  return json_tokens


if __name__ == '__main__':
  from pprint import pprint
  from pathlib import Path

  json_path = Path('./sample01.json')
  json_data = json_path.read_text(encoding='utf-8')
  json_data = '[{"nam e": "Taro", "age": 14, "check": true}, {"name": "Jiro", "age": 23, "check": false}, {"name": "Tom", "age": 16, "check": false}, {"name": null, "age": 14, "check": null}]'
  jjj = main()

