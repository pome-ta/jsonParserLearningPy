from re import compile
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


json_data = '[{"nam e": "Taro", "age": 14, "check": true}, {"name": "Jiro", "age": 23, "check": false}, {"name": "Tom", "age": 16, "check": false}]'

pattern = compile(r'([|]|{|}|:|,|")')

#print(json_data)

slice_data = pattern.split(json_data)
pprint(slice_data)

