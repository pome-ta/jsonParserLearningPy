from tokenTypes import TokenKind
from split_str02 import get_tokens
from lexer import get_lexer


def setup_deep(tkn, indeep):
  if tkn.kind in [TokenKind.LBRACE, TokenKind.LBRACKET]:
    tkn.deep = indeep
    indeep += 1
  if tkn.kind in [TokenKind.RBRACE, TokenKind.RBRACKET]:
    indeep -= 1
    tkn.deep = indeep
  return indeep


def setup_keytype(f_tkn, s_tkn):
  if s_tkn and s_tkn.kind == TokenKind.COLON:
    f_tkn.keytype = True


def set_attributes(tokens):
  deep = 1
  for index in range(len(tokens)):
    next_tkn = tokens[index + 1] if index + 1 < len(tokens) else None

    setup_keytype(tokens[index], next_tkn)
    deep = setup_deep(tokens[index], deep)


def get_deep_list(tokens):
  pool = []

  for n, tkn in enumerate(tokens):
    if tkn.deep:
      pool.append([n, tkn.deep])

  search = [p for p in pool]
  stack = []

  for p_index in range(len(pool)):
    p_deep = pool[p_index]

    if p_deep == None:
      continue

    indent = pool[p_index][1]
    search[p_index] = None
    pool[p_index] = None

    for s_index in range(len(pool)):
      s_deep = search[s_index]
      if s_deep and s_deep[1] == p_deep[1]:
        stack.append([p_deep[0], s_deep[0], indent])
        search[s_index] = None
        pool[s_index] = None
        break
  return stack


def set_indent(tokens, deeps):
  for s, e, i in deeps:
    ext_tokens = tokens[s:e + 1]
    for tkn in ext_tokens:
      tkn.indent = i


def get_token_list(strs):
  str_list = list(strs)
  tokens = get_lexer(get_tokens(str_list))
  return tokens


def get_dicts(tokens, indent=1):
  dic_key = None
  dic_value = None
  values = []
  stack = {}
  colon_flag = False
  children_flag = False
  for tkn in tokens:
    if tkn.indent == indent:
      if tkn.keytype:
        dic_key = tkn.value
      if tkn.kind == TokenKind.COLON:
        colon_flag = True
      if tkn.kind in [TokenKind.COMMA, TokenKind.RBRACE]:
        if children_flag:
          children_flag = False
          if values[0].kind == TokenKind.LBRACKET:
            dic_value = get_lists(values, indent + 1)
          elif values[0].kind == TokenKind.LBRACE:
            dic_value = get_dicts(values, indent + 1)
        stack.update({dic_key: dic_value})
        dic_key = None
        dic_value = None
        values = []
      if colon_flag and not (tkn.kind in [TokenKind.COMMA, TokenKind.COLON]):
        dic_value = tkn.value
    else:
      values.append(tkn)
      children_flag = True
  return stack


def get_lists(tokens, indent=1):
  list_value = None
  values = []
  stack = []
  children_flag = False
  for tkn in tokens:
    if tkn.indent == indent:
      if tkn.kind in [TokenKind.COMMA, TokenKind.RBRACKET]:
        if children_flag:
          children_flag = False
          if values[0].kind == TokenKind.LBRACKET:
            list_value = get_lists(values, indent + 1)
          elif values[0].kind == TokenKind.LBRACE:
            list_value = get_dicts(values, indent + 1)
        stack.append(list_value)
        list_value = None
        values = []
      if not (tkn.kind in [TokenKind.LBRACKET, TokenKind.COMMA]):
        list_value = tkn.value
    else:
      values.append(tkn)
      children_flag = True
  return stack


def get_obj(tokens):
  stack = None
  if tokens[0].kind == TokenKind.LBRACKET:
    stack = get_lists(tokens)
  elif tokens[0].kind == TokenKind.LBRACE:
    stack = get_dicts(tokens)
  return stack


def parse(strs):
  token_list = get_token_list(strs)
  set_attributes(token_list)
  deep_list = get_deep_list(token_list)
  set_indent(token_list, deep_list)
  for i in token_list:
    #print(f'indent->{i.indent} deep->{i.deep} \t{i.value}')
    pass
  obj = get_obj(token_list)
  a = 1
  return obj


if __name__ == '__main__':
  from pathlib import Path
  import json

  json_path = Path('./sample01.json')
  #json_path = Path('./sandbox01/sample01.json')
  json_data = json_path.read_text(encoding='utf-8')
  sample = json.loads(json_data)
  dump = parse(json_data)
  a = 1

