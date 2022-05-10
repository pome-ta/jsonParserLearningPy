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


def get_dict_block(tokens):
  pass


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


def pre_parse(strs):
  str_list = list(strs)
  tokens = get_tokens(str_list)
  lexer = get_lexer(tokens)
  indent_deep(lexer)
  set_keytype(lexer)
  return lexer


class JsonObj:
  def __init__(self, *pairs) -> None:
    self.pair = pairs


class Pair:
  def __init__(self) -> None:
    self.key = None
    self.value = None
    self.children = None


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


def set_keyvalue(tokens):

  sample_data = {
    "hoge": "fuga",
    "piyo": {
      "あ": "null",
      "い": "true",
      "う": "false"
    },
    "foo": "baa"
  }
  key = None
  value = []
  indent = 1
  deep = 1
  colon_flag = False
  children_flag = False
  pool = {}
  for index in range(len(tokens)):
    tkn = tokens[index]
    #indent = 
    if tkn.keytype:
      indent = tkn.indent
      key = tkn.value
    if tkn.indent == indent and tkn.kind == TokenKind.COLON:
      colon_flag = True
    if tkn.indent == indent and (tkn.kind == TokenKind.COMMA or
                                 tkn.kind == TokenKind.RBRACE):
      colon_flag = False
      if children_flag:
        value = set_keyvalue(value)
        children_flag = False
      pool.update({key: value})
      key = None
      value = []
    if tkn.indent == indent and colon_flag and not (
        tkn.kind == TokenKind.COMMA or tkn.kind == TokenKind.COLON):
      value = tkn.value
    elif tkn.indent != indent:
      value.append(tkn)
      children_flag = True

    index += 1
  print(pool)
  a = 1
  return pool


def get_dicts(tokens, indent=1):
  index = -1
  key = None
  values = []
  pool = {}
  colon_flag = False
  children_flag = False
  for _ in range(len(tokens)):
    index += 1
    tkn = tokens[index]
    print(tkn)
    if tkn.indent == indent:
      if tkn.keytype:
        key = tkn.value
        #continue
      if tkn.kind == TokenKind.COLON:
        colon_flag = True
        #continue
      if colon_flag and not (tkn.kind == TokenKind.COMMA or
                             tkn.kind == TokenKind.COLON):
        values = tkn.value
        #continue

      if tkn.kind == TokenKind.COMMA:
        if children_flag:
          values = get_dicts(values, indent + 1)
          children_flag = False
        pool.update({key: values})
        colon_flag = False
        key = None
        values = []
        continue
      if tkn.kind == TokenKind.RBRACE:
        if children_flag:
          values = get_dicts(values, indent + 1)
          children_flag = False
        pool.update({key: values})
        colon_flag = False
        key = None
        values = []
        return pool

    else:
      values.append(tkn)
      children_flag = True
      #continue
  #return pool


def main(strs):
  pre = pre_parse(strs)
  deep_list = get_deep_list(pre)
  set_indent(pre, deep_list)

  indent = max([n[2] for n in deep_list])
  sample_dict = {"hoge": "fuga", "foo": "baa"}
  a = 1
  return get_dicts(pre)


if __name__ == '__main__':
  test_data = '{"hoge":"fuga","piyo":{"あ":null, "い":true, "う":false}, "foo":"baa"}'
  #test_data = '{"hoge":"fuga", "foo": "baa"}'
  main = main(test_data)
  #sample_data = {"hoge": "fuga","piyo": {"あ": "null", "い": "true","う": "false"},"foo": "baa"}
  sample_data = {"hoge": "fuga", "foo": "baa"}
  a = 1

