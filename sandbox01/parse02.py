from tokenTypes import TokenKind
from split_str02 import get_tokens
from lexer import get_lexer
"""
再度、個々でラベリングをして
個別で対応、その後に統合する？
key は設定完了してる
value としての条件
  `:` 次の`,`
    連続している場合には、`{` か`[` が出現するはず
  `:` の次の`}`
インデントのグループ分けをした方がいい？
"""


def indent_deep(tokens):
  deep = 1
  for tkn in tokens:
    if tkn.kind == TokenKind.LBRACKET or tkn.kind == TokenKind.LBRACE:
      tkn.deep = deep
      deep += 1
    if tkn.kind == TokenKind.RBRACE or tkn.kind == TokenKind.RBRACKET:
      deep -= 1
      tkn.deep = deep


def set_keytype(tokens):
  for index in range(len(tokens)):
    tokens[index].keytype = False
    if tokens[index].kind == TokenKind.COLON:
      tokens[index - 1].keytype = True


def get_deep_list(tokens):
  pool = []
  for index in range(len(tokens)):
    if tokens[index].deep:
      pool.append([index, tokens[index].deep])

  search = [p for p in pool]
  stack = []
  for i in range(len(pool)):
    i_d = pool[i]
    if i_d == None:
      continue
    indent = pool[i][1]
    search[i] = None
    pool[i] = None
    for si in range(len(pool)):
      s_id = search[si]
      if s_id and s_id[1] == i_d[1]:
        stack.append([i_d[0], s_id[0], indent])
        search[si] = None
        pool[si] = None
        break
  return stack


"""
階層ができた
key 情報は持っている
value を抜き出したい
value は下階層も想定
key: value
key: value, key:value
value(key:value)
1 のkey の一つ前か、`}` まで
"""


def set_indent(tokens, deeps):
  for s, e, i in deeps:
    _token = tokens[s:e + 1]
    for tkn in _token:
      tkn.indent = i


def get_dicts(tokens, indent=1):
  key = None
  values = []
  pool = {}
  colon_flag = False
  children_flag = False
  for tkn in tokens:
    if tkn.indent == indent:
      if tkn.keytype:
        key = tkn.value
      if tkn.kind == TokenKind.COLON:
        colon_flag = True
      if tkn.kind == TokenKind.COMMA or tkn.kind == TokenKind.RBRACE:
        if children_flag:
          children_flag = False
          if values[0].kind == TokenKind.LBRACKET:
            values = get_lists(values, indent + 1)
          elif values[0].kind == TokenKind.LBRACE:
            values = get_dicts(values, indent + 1)

        pool.update({key: values})
        colon_flag = False
        key = None
        values = []

      if colon_flag and not (tkn.kind == TokenKind.COMMA or
                             tkn.kind == TokenKind.COLON):

        values = tkn.value
        # continue

    else:
      values.append(tkn)
      children_flag = True
      # continue
  return pool


def get_lists(tokens, indent=1):
  value = None
  values = []
  pool = []
  children_flag = False
  for tkn in tokens:
    if tkn.indent == indent:

      if tkn.kind == TokenKind.COMMA or tkn.kind == TokenKind.RBRACKET:
        #print(tkn)
        if children_flag:
          children_flag = False
          if values[0].kind == TokenKind.LBRACKET:
            value = get_lists(values, indent + 1)
          elif values[0].kind == TokenKind.LBRACE:
            value = get_dicts(values, indent + 1)
        pool.append(value)
        value = None
        values = []

      if tkn.kind != TokenKind.LBRACKET or tkn.kind != TokenKind.COMMA:
        value = tkn.value

    else:
      values.append(tkn)
      children_flag = True
  return pool


def py_parse(tokens):
  stack = None
  if tokens[0].kind == TokenKind.LBRACKET:
    stack = get_lists(tokens)
  elif tokens[0].kind == TokenKind.LBRACE:
    stack = get_dicts(tokens)
  return stack


def pre_parse(strs):
  str_list = list(strs)
  tokens = get_tokens(str_list)
  lexer = get_lexer(tokens)
  indent_deep(lexer)
  set_keytype(lexer)
  return lexer


def main(strs):
  pre = pre_parse(strs)
  deep_list = get_deep_list(pre)
  set_indent(pre, deep_list)
  r = py_parse(pre)
  #indent = max([n[2] for n in deep_list])

  a = 1
  return r


if __name__ == '__main__':
  from pathlib import Path

  json_path = Path('./sample01.json')
  #json_path = Path('./sandbox01/sample01.json')
  json_data = json_path.read_text(encoding='utf-8')
  #test_data = '{"hoge":"fuga","piyo":{"あ":null, "い":true, "う":false}, "foo":"baa"}'
  test_data = '{"hoge":"fuga","piyo":{"あ":null, "い":true, "う":false}, "list":[1,2,4],"foo":"baa"}'
  #test_data = '{"hoge":"fuga", "foo": "baa"}'
  mmain = main(test_data)
  #mmain = main(json_data)
  #sample_data = {"hoge": "fuga","piyo": {"あ": "null", "い": "true","う": "false"},"foo": "baa"}
  sample_data = {"hoge": "fuga", "foo": "baa"}
  a = 1

