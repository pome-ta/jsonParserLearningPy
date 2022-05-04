from tokenTypes import TokenKind
from split_str02 import get_tokens
from lexer import get_lexer



def simple_parse(token_list):
  pass

def main():
  json_chr_list = list(json_data)
  pre_tokens = get_tokens(json_chr_list)
  json_tokens = get_lexer(pre_tokens)
  return json_tokens


if __name__ == '__main__':
  from pprint import pprint
  from pathlib import Path

  json_path = Path('./sample01.json')
  json_data = json_path.read_text(encoding='utf-8')
  jjj = main()

