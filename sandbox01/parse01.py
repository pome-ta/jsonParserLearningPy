from tokenTypes import TokenKind
from split_str02 import get_tokens
from lexer import get_lexer


def pre_parse(strs):
  str_list = list(strs)
  tokens = get_tokens(str_list)
  lexer = get_lexer(tokens)
  return lexer


def set_keytype(tokens):
  for index in range(len(tokens)):
    tokens[index].keytype = False
    if tokens[index].kind == TokenKind.COLON:
      tokens[index - 1].keytype = True


def create_dicts(tokens):
  set_keytype(tokens)
  key = None
  value = None
  for tkn in tokens:
    if tkn.kind == TokenKind.LBRACE:
      pass


def main(strs):
  pre = pre_parse(strs)
  create_dicts(pre)
  return None


if __name__ == '__main__':
  test_data = '{"hoge":"fuga", "foo":"baa"}'
  main = main(test_data)

