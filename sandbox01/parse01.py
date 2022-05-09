from tokenTypes import TokenKind
from split_str02 import get_tokens
from lexer import get_lexer


def pre_parse(strs):
  str_list = list(strs)
  tokens = get_tokens(str_list)
  lexer = get_lexer(tokens)
  return lexer
  
def create_dicts(tokens):
  for tkn in tokens:
    if tkn.kind == TokenKind.LBRACE:
      pass


def main(strs):
  pre = pre_parse(strs)
  create_dicts(pre)
  return None
  

if __name__ == '__main__':
  test_data = '{"hoge":"fuga"}'
  main = main(test_data)

