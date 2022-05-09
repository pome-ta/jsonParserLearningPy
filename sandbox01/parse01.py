from tokenTypes import TokenKind
from split_str02 import get_tokens
from lexer import get_lexer


class JsonObjs:
  def __init__(self):
    pass

if __name__ == '__main__':
  from pprint import pprint
  from pathlib import Path

  json_path = Path('./sample01.json')
  #json_path = Path('./sandbox01/sample01.json')
  json_data = json_path.read_text(encoding='utf-8')
