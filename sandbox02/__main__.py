from enum import Enum, auto


class TokenType(Enum):
  NUMBER = auto()  # 数値
  STRING = auto()  # 文字列
  BOOLEAN = auto()  # true or false
  NULL = auto()  # null

  L_BRACKET = auto()  # [
  R_BRACKET = auto()  # ]
  L_BRACE = auto()  # {
  R_BRACE = auto()  # }
  COLON = auto()  # :
  COMMA = auto()  # ,


class Token:
  def __init__(self, type, value=None):
    self.type: TokenType = type
    self.value: str = value
    self.obj_key: bool = False
    self.nest: int = None
    self.indent: int = None

  def __str__(self):
    return str(self.value)


# xxx: 無駄？
# xxx: 同じものとして担保してない、、、？
def _get_symbol_dict() -> dict:
  return {
    '[': Token(TokenType.L_BRACKET, '['),
    ']': Token(TokenType.R_BRACKET, ']'),
    '{': Token(TokenType.L_BRACE, '{'),
    '}': Token(TokenType.R_BRACE, '}'),
    ':': Token(TokenType.COLON, ':'),
    ',': Token(TokenType.COMMA, ','),
  }


def _get_bool2null_dict() -> dict:
  return {
    't': Token(TokenType.BOOLEAN, 'true'),
    'f': Token(TokenType.BOOLEAN, 'false'),
    'n': Token(TokenType.NULL, 'null'),
  }


flag_symbols = _get_symbol_dict().keys()
flag_bool2null = _get_bool2null_dict().keys()
zero2nine_strs = [str(n) for n in range(10)]
# xxx: `e`, `E` は不要かな？
flag_numbers = [*zero2nine_strs, '.', '-', 'e', 'E']


def _check_bool2null(chars: str, value: str) -> None:
  if not (chars == value):
    # xxx: エラー処理
    raise Exception
    print(f'error!: {chars}')


def _get_strings_step(tail_list: list) -> tuple:
  quotation_flag = False
  for n, string in enumerate(tail_list):
    if string == '"':
      if n and tail_list[n - 1] == '\\': continue
      if quotation_flag: break
      quotation_flag = True
  str_value = ''.join(tail_list[:n + 1])
  return str_value, len(str_value)


def _get_numbers_step(tail_list):
  # xxx: `10,000` みたいな表現できない
  end = [',', '}', ']', '\n']
  for n, number in enumerate(tail_list):
    if number in end: break
  num_value = ''.join(tail_list[:n])
  return num_value, len(num_value)

# xxx: `for` するから遅くなる？
def _get_bools2null_step(tail_list: list) -> tuple:
  
  for string in tail_list:
    step = 5 if string == 'f' else 4
    if string == 't':
      bool_null = ''.join(tail_list[:step])
      if bool_null == 'true': raise Exception
    elif string == 'f':
      bool_null = ''.join(tail_list[:step])
      if bool_null == 'false': raise Exception
    elif string == 'n':
      bool_null = ''.join(tail_list[:step])
      if bool_null == 'null': raise Exception
    else:
      raise Exception
        
      
  



def get_tokens(strs: str) -> list:
  char_list = list(strs)
  length = char_list.__len__()
  tokens = []

  index = 0
  for _ in range(length):
    if index >= length: break
    char = char_list[index]

    if char.isspace():
      index += 1
      continue  # 空白は早々に棄却

    if char in flag_symbols:
      tkn = _get_symbol_dict()[char]
      add_index = 1

    elif char in flag_bool2null:
      # xxx: ちゃんと入ってから返してあげるべき？
      tkn = _get_bool2null_dict()[char]
      add_index = 5 if char == 'f' else 4
      bool_or_null = ''.join(char_list[index:index + add_index])
      _check_bool2null(bool_or_null, tkn.value)

    elif char == '"':
      value, add_index = _get_strings_step(char_list[index:])
      tkn = Token(TokenType.STRING, value)

    elif char in flag_numbers:
      value, add_index = _get_numbers_step(char_list[index:])
      tkn = Token(TokenType.NUMBER, value)

    # xxx: エラー処理
    else:
      raise Exception
      print(f'error!: {char}')
    index += add_index
    tokens.append(tkn)
  return tokens


if __name__ == '__main__':
  from pathlib import Path

  json_path = Path('./sample02.json')
  json_str = json_path.read_text(encoding='utf-8')
  t = Token(TokenType.COLON, ':')
  main = get_tokens(json_str)

