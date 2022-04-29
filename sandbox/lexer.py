from re import compile, findall
from enum import Enum
from typing import List

from pprint import pprint


class Token(Enum):
  String = str


class BloodType(Enum):
  A = 'A型'
  B = 'B型'
  O = 'O型'
  AB = 'AB型'

  def __str__(self):
    return self.name

  @classmethod
  def show_all(cls) -> List[str]:
    return list(map(lambda c: c.value, cls))


b = BloodType('A型')

r = '''{
   "number":123,
   "bool ean":true,
   "string":"togatoga",
   "object":{
      "number":2E10
   }
}
'''

json_data = '[{"nam e": "Taro", "age": 14, "check": true}, {"name": "Jiro", "age": 23, "check": false}, {"name": "Tom", "age": 16, "check": false}]'

json_chr_list = list(json_data)
value = ''
flag = 0
tokens = []

for n, chr in enumerate(json_chr_list):
  if chr == '[':
    tokens.append(chr)
    continue
  elif chr == '{':
    tokens.append(chr)
    continue
  elif chr == ':':
    tokens.append(chr)
    continue
  elif chr == ',':
    tokens.append(chr)
    continue
  elif chr == '}':
    tokens.append(chr)
    continue
  elif chr == ']':
    tokens.append(chr)
    continue
  elif chr == '"':
    #flag = 0 if flag else 1
    value += chr
    if flag:
      flag = 0
      tokens.append(value)
      value = ''
      continue
    flag = 1
  else:
    value += chr

#pattern = compile(r'([|]|{|}|:|,|")')
#pattern = compile(r'([|]|{|}|:|,)')
#pattern = compile(r'([|]|{|}|:|,|\n)')
#pattern = compile(r'(\[|\]|\{|\}|:|,|\n)')
pattern = compile(r'(?=(\[|\]|\{|\}|:|,))')
#pattern = compile(r'"(.+?)"')

pattern = compile(r'([|]|{|}|:|,)')

#print(json_data)

slice_data = pattern.split(json_data)
#slice_data = pattern.split(r)
filter_data = list(filter(lambda f: bool(f), slice_data))
#slice_data = findall('[^\}|,]+}?', json_data)
#slice_data = findall(r'[^:]+:?', json_data)
#[print(t) for t in filter_data]
'''
print(slice_data[30])
print(len(slice_data[30]))
print(bool(slice_data[30]))
print(slice_data[32])
print(len(slice_data[32]))
print(bool(slice_data[32]))
'''
#list_str = list(r)
#print(list_str)

