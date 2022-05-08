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


class Node:
  def __init__(self, left, objs, right, children=None):
    self.left: str = left
    self.objs: str = objs
    self.right: str = right
    self.children: Node = children

  def select_type(self):
    if self.left == '{':
      self.core_stack = {}
    if self.left == '[':
      self.core_stack = []

  def set_objs(self):
    pass


def setup(lists, types, indeep):
  if types == TokenKind.LBRACKET:
    pass
  if types == TokenKind.LBRACE:
    pass


def set_key(lists):
  pass


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

  pprint(stack)
  #return stack


# dict_key
# dict_value
#   dict_key
#   list_value
# list_value
#   dict_key
#   list_value


def set_deep_list(lists):
  pool = []
  for index in range(len(lists)):
    if lists[index].deep:
      print(index, lists[index].deep)
      pool.append([index, lists[index].deep])
      
  search = [p for p in pool]
  stack = []
  for i in range(len(pool)):
    i_d = pool[i]
    if i_d == None: continue
    #if len(set(search)) <= 1: break
    search[i] = None
    pool[i] = None
    for si in range(len(pool)):
      s_id = search[si]
      if s_id and s_id[1] == i_d[1]:
        stack.append([i_d[0], s_id[0]])
        search[si] = None
        pool[si] = None
        
        break
    
        
  print(stack)
  #print(search)
    
    
    
    
    
    
      

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
    # todo: 辞書か配列にある前提
    if 0 == index and (tkn.kind == TokenKind.LBRACE or tkn.kind == TokenKind.LBRACKET):
      if tkn.kind == TokenKind.LBRACE:
        stack = dict()
      if tkn.kind == TokenKind.LBRACKET:
        stack = list()
    if tkn.type == 'dict_key':
      key = tkn.value
    index += 1

  return stack



class JsonParser:
  pass


class PyAst:
  pass


def main():
  json_chr_list = list(json_data)
  pre_tokens = get_tokens(json_chr_list)
  json_tokens = get_lexer(pre_tokens)
  indent_deep(json_tokens)
  setup_dictkey(json_tokens)
  set_deep_list(json_tokens)

  return json_tokens, set_json(json_tokens)


if __name__ == '__main__':
  from pprint import pprint
  from pathlib import Path

  json_path = Path('./sample01.json')
  #json_path = Path('./sandbox01/sample01.json')
  json_data = json_path.read_text(encoding='utf-8')
  #json_data = '[{"nam e": "Taro", "age": 14, "check": true}, {"name": "Jiro", "age": 23, "check": false}, {"name": "Tom", "age": 16, "check": false}, {"name": null, "age": 14, "check": null}]'
  jjj, jptree = main()

