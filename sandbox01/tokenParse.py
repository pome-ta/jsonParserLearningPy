from tokenTypes import TokenKind
from split_str02 import get_tokens
from lexer import get_lexer


def simple_parse(token_list):
  #indent_deep(token_list)
  deep = 0
  index = 0
  for _ in range(len(token_list)):
    tkn = token_list[index]
    if tkn.deep:
      deep = tkn.deep
      index += 1
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
  deep = 1
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

  #pprint(stack)
  #return stack

  # dict_key
  # dict_value
  #   dict_key
  #   list_value
  # list_value
  #   dict_key
  #   list_value


def get_deep_list(lists):
  pool = []
  for index in range(len(lists)):
    if lists[index].deep:
      #print('ffff', index, lists[index].deep)
      pool.append([index, lists[index].deep])

  search = [p for p in pool]
  stack = []
  for i in range(len(pool)):
    i_d = pool[i]
    if i_d == None: continue
    #if len(set(search)) <= 1: break
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
  #print(search)
  return stack


def setup_dictkey(lists):
  for index in range(len(lists)):
    lists[index].type = None
    if lists[index].kind == TokenKind.COLON:
      lists[index - 1].type = 'dict_key'


def set_json(lists):
  stack = None
  index = 0
  key = None
  value = None
  for _ in range(len(lists)):
    tkn = lists[index]
    # todo: ??????????????????????????????
    if 0 == index and (tkn.kind == TokenKind.LBRACE or
                       tkn.kind == TokenKind.LBRACKET):
      if tkn.kind == TokenKind.LBRACE:
        stack = dict()
      if tkn.kind == TokenKind.LBRACKET:
        stack = list()
    if tkn.type == 'dict_key':
      key = tkn.value
    index += 1

  return stack


class ArrayObj:
  def __init__(self, tokens):
    self.tokens = tokens


class DictObj:
  def __init__(self, tokens):
    self.tokens = tokens


def list_dic(t_lists, d_lists):
  pool = []
  #print(d_lists)
  #print(t_lists)
  for s, e in d_lists:
    if t_lists[s].kind == TokenKind.LBRACKET:
      pool.append(ArrayObj(t_lists[s + 1:e]))
    if t_lists[s].kind == TokenKind.LBRACE:
      pool.append(DictObj(t_lists[s + 1:e]))
  return pool


def index_list(deeps):
  s = ''
  for i in deeps:
    tab = (i[2] - 1) * '\t'
    s += tab + str(i) + '\n'
  print(s)


def main():
  json_chr_list = list(json_data)
  pre_tokens = get_tokens(json_chr_list)
  json_tokens = get_lexer(pre_tokens)
  indent_deep(json_tokens)
  setup_dictkey(json_tokens)
  deep_list = get_deep_list(json_tokens)
  index_list(deep_list)

  #set_json(json_tokens)
  return json_tokens, None  #list_dic(json_tokens, deep_list)


if __name__ == '__main__':
  from pprint import pprint
  from pathlib import Path

  json_path = Path('./sample01.json')
  #json_path = Path('./sandbox01/sample01.json')
  json_data = json_path.read_text(encoding='utf-8')
  #json_chr_list = list(json_data)
  #json_data = '[{"nam e": "Taro", "age": 14, "check": true}, {"name": "Jiro", "age": 23, "check": false}, {"name": "Tom", "age": 16, "check": false}, {"name": null, "age": 14, "check": null}]'
  jjj, jptree = main()

  for j in jjj:
    j
    #print(j)

